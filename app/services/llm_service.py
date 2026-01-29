"""
KLTN_UIT_BE LLM Service - Optimized
Integration with llama.cpp server with caching and async support
"""
import hashlib
import json
import logging
from typing import Any, Dict, List, Optional
from functools import lru_cache

import httpx
from app.config import get_settings

logger = logging.getLogger(__name__)


class LLMServiceError(Exception):
    """Custom exception for LLM service errors"""
    pass


class LLMService:
    """
    Service for interacting with llama.cpp server
    Optimized with connection pooling and response caching
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
        
        # Response cache for identical requests
        self._response_cache: Dict[str, str] = {}
        self._cache_max_size = 256
    
    @property
    def client(self) -> httpx.Client:
        """Get or create HTTP client with connection pooling"""
        if self._client is None:
            self._client = httpx.Client(
                timeout=httpx.Timeout(self.timeout, connect=10.0),
                limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),
                follow_redirects=True
            )
        return self._client
    
    def close(self):
        """Close the HTTP client"""
        if self._client is not None:
            self._client.close()
            self._client = None
    
    def is_available(self) -> bool:
        """Check if LLM server is available"""
        try:
            response = self.client.get(
                f"{self.base_url}/v1/models",
                headers=self._get_headers(),
                timeout=5.0
            )
            return response.status_code == 200
        except Exception as e:
            logger.error(f"LLM server check failed: {e}")
            return False
    
    def _get_headers(self) -> Dict[str, str]:
        """Get headers for API requests"""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _get_cache_key(self, messages: List[Dict[str, str]], temperature: float) -> str:
        """Generate cache key from messages"""
        content = json.dumps(messages, ensure_ascii=False, sort_keys=True) + str(temperature)
        return hashlib.md5(content.encode()).hexdigest()
    
    def _cache_response(self, key: str, response: str):
        """Cache response with size limit"""
        if len(self._response_cache) >= self._cache_max_size:
            # Remove oldest entries (simple FIFO)
            oldest = list(self._response_cache.keys())[:self._cache_max_size // 4]
            for k in oldest:
                del self._response_cache[k]
        self._response_cache[key] = response
    
    def get_completion(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        use_cache: bool = True
    ) -> str:
        """
        Get chat completion from LLM with caching
        
        Args:
            messages: List of messages [{role: "system"|"user", content: "..."}]
            temperature: Override for temperature
            max_tokens: Override for max tokens
            use_cache: Whether to use response cache
        
        Returns:
            The text content of the completion
        """
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens
        
        # Check cache first
        if use_cache and temp == 0:
            cache_key = self._get_cache_key(messages, temp)
            if cache_key in self._response_cache:
                logger.debug("Cache hit for LLM request")
                return self._response_cache[cache_key]
        
        url = f"{self.base_url}/v1/chat/completions"
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temp,
            "max_tokens": tokens,
            "stream": False,
            "response_format": {"type": "json_object"}
        }
        
        try:
            response = self.client.post(url, headers=self._get_headers(), json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            if "choices" not in result or len(result["choices"]) == 0:
                raise LLMServiceError("Invalid response: no choices")
            
            content = result["choices"][0].get("message", {}).get("content", "")
            if not content:
                raise LLMServiceError("Empty content in response")
            
            # Cache response for temperature=0 (deterministic)
            if use_cache and temp == 0:
                self._cache_response(cache_key, content)
            
            return content
            
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error: {e.response.status_code}")
            raise LLMServiceError(f"LLM server error: {e.response.status_code}")
        except httpx.RequestError as e:
            logger.error(f"Request error: {e}")
            raise LLMServiceError(f"Connection failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise LLMServiceError(f"LLM error: {e}")
    
    def get_prediction(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.0
    ) -> str:
        """Get prediction using system + user prompts"""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return self.get_completion(messages=messages, temperature=temperature)
    
    def clear_cache(self):
        """Clear response cache"""
        self._response_cache.clear()
        logger.info("LLM response cache cleared")
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        return {
            "size": len(self._response_cache),
            "max_size": self._cache_max_size
        }


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
