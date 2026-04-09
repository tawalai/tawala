# utils/http.py
import requests

class HttpClient:
    def __init__(self, config):
        self.base_url = config.base_url
        self.api_key = config.api_key

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get(self, path, params=None):
        return requests.get(self.base_url + path, headers=self._headers(), params=params).json()

    def post(self, path, json=None):
        return requests.post(self.base_url + path, headers=self._headers(), json=json).json()