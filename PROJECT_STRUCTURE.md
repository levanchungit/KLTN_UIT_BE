# KLTN_UIT_BE - AI Backend for Transaction Classification
# FastAPI + llama.cpp Integration

app/
├── __init__.py
├── main.py                 # FastAPI app entry point
├── config.py              # Configuration loader
├── routes/
│   ├── __init__.py
│   └── predict.py         # /predict endpoint
├── services/
│   ├── __init__.py
│   ├── llm_service.py     # llama.cpp integration
│   ├── preprocessing.py   # Text preprocessing
│   └── postprocessing.py  # JSON parsing & validation
├── schemas/
│   ├── __init__.py
│   └── request_response.py # Pydantic models
└── prompts/
    ├── __init__.py
    └── system_prompts.py  # Prompt templates

tests/
├── __init__.py
├── test_api.py
└── test_preprocessing.py

config.yaml
requirements.txt
README.md
.env.example
