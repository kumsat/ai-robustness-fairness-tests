import os
from dataclasses import dataclass

import requests
from dotenv import load_dotenv

load_dotenv()


@dataclass
class ApiClient:
    """Simple HTTP client for the robustness/fairness text API."""

    base_url: str = os.getenv("API_URL", "http://127.0.0.1:5002/classify")
    health_url: str = os.getenv("HEALTHCHECK_URL", "http://127.0.0.1:5002/health")

    def classify_text(self, text: str) -> requests.Response:
        payload = {"text": text}
        return requests.post(self.base_url, json=payload, timeout=5)

    def healthcheck(self) -> requests.Response:
        return requests.get(self.health_url, timeout=5)

