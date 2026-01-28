"""
Direct test script to evaluate model performance on real dataset
Uses the model services directly without requiring the API server
"""
import pandas as pd
import json
import time
import sys
from pathlib import Path
from typing import Dict, List
import logging

# Add app directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app.config import load_config, get_settings
from app.services.llm_service import get_llm_service, LLMServiceError
from app.services.preprocessing import normalize_text
from app.services.postprocessing import process_llm_response, PostprocessingError
from app.prompts.system_prompts import build_prompts

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
DATASET_PATH = r"D:\FPT\Github\KLTN_UIT_BE\test_dataset_500_unique_from_source_utf8_bom.csv"
OUTPUT_PATH = "test_results_direct.csv"
MAX_REQUESTS = 50  # Start with 50 to test, set to None for all

def load_dataset(filepath: str) -> pd.DataFrame:
    """Load the test dataset from CSV"""
    logger.info(f"Loading dataset from {filepath}")
    df = pd.read_csv(filepath, encoding='utf-8-sig')
    logger.info(f"Loaded {len(df)} records")
    logger.info(f"Columns: {df.columns.tolist()}")
    return df

def make_prediction(text: str, llm_service, valid_categories: List[str], valid_types: List[str]) -> Dict:
    """Make a prediction using the model services directly"""
    try:
        # Preprocess text
        normalized_text = normalize_text(text)
        
        # Build prompts
        system_prompt, user_prompt = build_prompts(normalized_text, valid_categories)
        
        # Get LLM prediction
        raw_output = llm_service.get_prediction(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.0
        )
        
        # Postprocess response
        prediction = process_llm_response(
            raw_output=raw_output,
            valid_categories=valid_categories,
            valid_types=valid_types,
            fix_invalid=True
        )
        
        return {
            "amount": prediction.get("amount", 0),
            "category": prediction.get("category", "Khác"),
            "type": prediction.get("type", "Chi phí"),
            "confidence": prediction.get("confidence", 0.5),
            "raw_output": raw_output
        }
    except (LLMServiceError, PostprocessingError) as e:
        logger.error(f"Prediction error: {e}")
        return {"error": str(e)}
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {"error": str(e)}

def calculate_accuracy(true_value, predicted_value) -> bool:
    """Check if prediction matches true value"""
    if pd.isna(true_value) or predicted_value is None:
        return False
    return str(true_value).strip().lower() == str(predicted_value).strip().lower()

def calculate_amount_error(true_amount, predicted_amount) -> float:
    """Calculate absolute percentage error for amount"""
    if pd.isna(true_amount) or predicted_amount is None or true_amount == 0:
        return float('inf')
    return abs(true_amount - predicted_amount) / true_amount * 100

def run_tests(df: pd.DataFrame, llm_service, settings, max_requests: int = None) -> pd.DataFrame:
    """Run predictions on all records in the dataset"""
    results = []
    
    if max_requests:
        df = df.head(max_requests)
    
    total = len(df)
    valid_categories = settings.app.default_categories
    valid_types = settings.app.transaction_types
    
    logger.info(f"Testing {total} transactions...")
    logger.info(f"Valid categories: {valid_categories}")
    logger.info(f"Valid types: {valid_types}")
    
    for idx, row in df.iterrows():
        progress = idx + 1
        logger.info(f"Processing {progress}/{total}: {row['text'][:60]}...")
        
        # Make prediction
        start_time = time.time()
        prediction = make_prediction(row['text'], llm_service, valid_categories, valid_types)
        elapsed_time = time.time() - start_time
        
        if "error" in prediction:
            logger.error(f"Failed to predict: {prediction['error']}")
            results.append({
                'index': idx,
                'text': row['text'],
                'true_amount': row['amount_vnd'],
                'true_category': row['category'],
                'true_type': row['type'],
                'predicted_amount': None,
                'predicted_category': None,
                'predicted_type': None,
                'confidence': None,
                'amount_match': False,
                'category_match': False,
                'type_match': False,
                'amount_error_pct': None,
                'response_time': elapsed_time,
                'error': prediction['error']
            })
            continue
        
        # Calculate accuracy metrics
        amount_match = (row['amount_vnd'] == prediction.get('amount'))
        category_match = calculate_accuracy(row['category'], prediction.get('category'))
        type_match = calculate_accuracy(row['type'], prediction.get('type'))
        amount_error_pct = calculate_amount_error(row['amount_vnd'], prediction.get('amount'))
        
        results.append({
            'index': idx,
            'text': row['text'],
            'true_amount': row['amount_vnd'],
            'true_category': row['category'],
            'true_type': row['type'],
            'predicted_amount': prediction.get('amount'),
            'predicted_category': prediction.get('category'),
            'predicted_type': prediction.get('type'),
            'confidence': prediction.get('confidence'),
            'amount_match': amount_match,
            'category_match': category_match,
            'type_match': type_match,
            'amount_error_pct': amount_error_pct if amount_error_pct != float('inf') else None,
            'response_time': elapsed_time,
            'error': None
        })
        
        # Progress update every 10 items
        if progress % 10 == 0:
            logger.info(f"Progress: {progress}/{total} ({progress/total*100:.1f}%)")
    
    return pd.DataFrame(results)

def print_summary(results_df: pd.DataFrame):
    """Print summary statistics"""
    print("\n" + "="*80)
    print("TEST RESULTS SUMMARY")
    print("="*80)
    
    total = len(results_df)
    successful = len(results_df[results_df['error'].isna()])
    failed = total - successful
    
    print(f"\nTotal requests: {total}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    if successful > 0:
        # Amount accuracy
        amount_matches = results_df['amount_match'].sum()
        amount_accuracy = (amount_matches / successful) * 100
        print(f"\n{'='*40}")
        print(f"AMOUNT ACCURACY: {amount_accuracy:.2f}% ({amount_matches}/{successful})")
        print(f"{'='*40}")
        
        # Amount error statistics
        valid_errors = results_df[results_df['amount_error_pct'].notna()]['amount_error_pct']
        if len(valid_errors) > 0:
            print(f"Mean Amount Error: {valid_errors.mean():.2f}%")
            print(f"Median Amount Error: {valid_errors.median():.2f}%")
            print(f"Max Amount Error: {valid_errors.max():.2f}%")
        
        # Category accuracy
        category_matches = results_df['category_match'].sum()
        category_accuracy = (category_matches / successful) * 100
        print(f"\n{'='*40}")
        print(f"CATEGORY ACCURACY: {category_accuracy:.2f}% ({category_matches}/{successful})")
        print(f"{'='*40}")
        
        # Type accuracy
        type_matches = results_df['type_match'].sum()
        type_accuracy = (type_matches / successful) * 100
        print(f"\n{'='*40}")
        print(f"TYPE ACCURACY: {type_accuracy:.2f}% ({type_matches}/{successful})")
        print(f"{'='*40}")
        
        # Overall accuracy (all three correct)
        all_correct = results_df[
            results_df['amount_match'] & 
            results_df['category_match'] & 
            results_df['type_match']
        ]
        overall_accuracy = (len(all_correct) / successful) * 100
        print(f"\n{'='*40}")
        print(f"OVERALL ACCURACY (All Correct): {overall_accuracy:.2f}% ({len(all_correct)}/{successful})")
        print(f"{'='*40}")
        
        # Confidence statistics
        avg_confidence = results_df['confidence'].mean()
        print(f"\nAverage Confidence: {avg_confidence:.4f}")
        
        # Response time
        avg_response_time = results_df['response_time'].mean()
        print(f"Average Response Time: {avg_response_time:.3f}s")
        print(f"Total Processing Time: {results_df['response_time'].sum():.1f}s")
        
        # Category distribution
        print("\n" + "-"*40)
        print("Predicted Category Distribution:")
        print("-"*40)
        category_dist = results_df['predicted_category'].value_counts()
        for cat, count in category_dist.items():
            pct = (count / successful) * 100
            print(f"  {cat}: {count} ({pct:.1f}%)")
        
        # Show some examples of errors
        print("\n" + "-"*40)
        print("Sample of Incorrect Predictions:")
        print("-"*40)
        incorrect = results_df[~(results_df['amount_match'] & results_df['category_match'] & results_df['type_match'])]
        if len(incorrect) > 0:
            for i, row in incorrect.head(5).iterrows():
                print(f"\nText: {row['text'][:70]}...")
                print(f"  True: {row['true_amount']} VND, {row['true_category']}, {row['true_type']}")
                print(f"  Pred: {row['predicted_amount']} VND, {row['predicted_category']}, {row['predicted_type']}")
    
    print("\n" + "="*80)

def main():
    """Main test execution"""
    try:
        # Load configuration
        logger.info("Loading configuration...")
        config = load_config()
        settings = get_settings()
        
        # Initialize LLM service
        logger.info("Initializing LLM service...")
        llm_service = get_llm_service()
        
        if not llm_service.is_available():
            logger.error("LLM service is not available. Please start llama.cpp server first.")
            logger.error(f"Expected URL: {settings.llm.base_url}")
            return
        
        logger.info("LLM service is ready!")
        logger.info(f"Model: {settings.llm.model}")
        logger.info(f"LLM Server URL: {settings.llm.base_url}")
        
        # Load dataset
        df = load_dataset(DATASET_PATH)
        
        # Run tests
        results_df = run_tests(df, llm_service, settings, MAX_REQUESTS)
        
        # Save results
        logger.info(f"\nSaving results to {OUTPUT_PATH}")
        results_df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
        
        # Print summary
        print_summary(results_df)
        
        logger.info(f"\nDetailed results saved to: {OUTPUT_PATH}")
        
    except FileNotFoundError:
        logger.error(f"Dataset file not found: {DATASET_PATH}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)

if __name__ == "__main__":
    main()
