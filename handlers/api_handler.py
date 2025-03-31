from typing import Optional
import requests

class OpenAIHandler:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def _make_request(self, endpoint: str, data: dict, files: Optional[dict] = None) -> Optional[dict]:
        try:
            response = requests.post(endpoint, 
                                  headers=self.headers, 
                                  json=data if not files else None,
                                  files=files)
            response.raise_for_status()
            return response.json() if not files else response.content
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {str(e)}")
            return None