"""
KLTN_UIT_BE LLM Service
Integration with llama.cpp server (OpenAI-compatible API)
"""
import json
import logging
from typing import Any, Dict, List, Optional

import httpx
from app.config import get_settings

logger = logging.getLogger(__name__)
class LLMServiceError(Exception):
    """Custom exception for LLM service errors"""
    pass
class LLMService:
    """
    Service for interacting with llama.cpp server
    Provides OpenAI-compatible API for chat completions
    """
    def __init__(self):
        """Initialize LLM service with configuration"""
        self.settings = get_settings()
        self.base_url = self.settings.llm.base_url
        self.api_key = self.settings.llm.api_key
        self.model = self.settings.llm.model
        self.temperature = self.settings.llm.temperature
        self.max_tokens = self.settings.llm.max_tokens
        self.timeout = self.settings.llm.timeout
        self._client: Optional[httpx.Client] = None
    @property
    def client(self) -> httpx.Client:
        """Get or create HTTP client"""
        if self._client is None:
            self._client = httpx.Client(
                timeout=self.timeout,
                follow_redirects=True
            )
        return self._client
    def close(self):
        """Close the HTTP client"""
        if self._client is not None:
            self._client.close()
            self._client = None
    def is_available(self) -> bool:
        """
        Check if LLM server is available
        
        Returns:
            True if server is reachable, False otherwise
        """
        try:
            # Try to call the models endpoint
            response = self.client.get(
                f"{self.base_url}/v1/models",
                headers=self._get_headers()
            )
            return response.status_code == 200
        except Exception as e:
            logger.error(f"LLM server availability check failed: {e}")
            return False
    def _get_headers(self) -> Dict[str, str]:
        """Get headers for API requests"""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    def _get_chat_completion_payload(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Build payload for chat completion request
        
        Args:
            messages: List of message objects with role and content
            temperature: Override for temperature setting
            max_tokens: Override for max tokens setting
        
        Returns:
            Payload dictionary for API request
        """
        return {
            "model": self.model,
            "messages": messages,
            "temperature": temperature if temperature is not None else self.temperature,
            "max_tokens": max_tokens if max_tokens is not None else self.max_tokens,
            "stream": False,
            "response_format": {"type": "json_object"}  # Enable JSON mode if supported
        }
    def get_completion(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Get chat completion from LLM
        
        Args:
            messages: List of messages [{role: "system"|"user", content: "..."}]
            temperature: Override for temperature (0 for deterministic output)
            max_tokens: Override for max tokens
        
        Returns:
            The text content of the completion
        
        Raises:
            LLMServiceError: If API call fails or returns invalid response
        """
        url = f"{self.base_url}/v1/chat/completions"
        payload = self._get_chat_completion_payload(
            messages, temperature, max_tokens
        )
        try:
            logger.debug(f"Sending request to LLM server: {url}")
            logger.debug(f"Messages: {json.dumps(messages, ensure_ascii=False)[:200]}...")
            
            response = self.client.post(
                url,
                headers=self._get_headers(),
                json=payload
            )
            response.raise_for_status()
            
            result = response.json()
            logger.debug(f"LLM response received: {json.dumps(result, ensure_ascii=False)[:200]}...")
            
            # Extract content from OpenAI-compatible response
            if "choices" not in result or len(result["choices"]) == 0:
                raise LLMServiceError("Invalid response: no choices in response")
            
            choice = result["choices"][0]
            if "message" not in choice:
                raise LLMServiceError("Invalid response: no message in choice")
            
            content = choice["message"].get("content", "")
            if not content:
                raise LLMServiceError("Empty content in response")
            
            return content
            
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error from LLM server: {e.response.status_code} - {e.response.text}")
            raise LLMServiceError(f"LLM server returned error: {e.response.status_code}")
        except httpx.RequestError as e:
            logger.error(f"Request error to LLM server: {e}")
            raise LLMServiceError(f"Failed to connect to LLM server: {e}")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM response as JSON: {e}")
            raise LLMServiceError(f"Invalid JSON response from LLM: {e}")
        except Exception as e:
            logger.error(f"Unexpected error in LLM service: {e}")
            raise LLMServiceError(f"LLM service error: {e}")
    def get_prediction(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.0
    ) -> str:
        """
        Get prediction response using system + user prompts
        
        Args:
            system_prompt: System instruction
            user_prompt: User query
            temperature: Temperature for generation (0 for deterministic)
        
        Returns:
            The text content of the prediction
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return self.get_completion(
            messages=messages,
            temperature=temperature,
            max_tokens=self.max_tokens
        )
# =====================
# Service Singleton
# =====================
_llm_service: Optional[LLMService] = None
def get_llm_service() -> LLMService:
    """Get or create LLM service instance"""
    global _llm_service
    if _llm_service is None:
        _llm_service = LLMService()
    return _llm_service
def close_llm_service():
    """Close the LLM service"""
    global _llm_service
    if _llm_service is not None:
        _llm_service.close()
        _llm_service = None
