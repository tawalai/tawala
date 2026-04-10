# utils/http.py
import requests

class HttpClient:
    def __init__(self, config):
        self.base_url = config.base_url
        self.api_key = config.api_key

    def _headers(self):
        return {
            "Authorization": f"ApiKey {self.api_key}",
            "Content-Type": "application/json"
        }

    def get(self, path, params=None):
        response = requests.get(self.base_url + path, headers=self._headers(), params=params)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            raise requests.HTTPError(
                f"GET {response.url} failed with status {response.status_code}: {response.text}") from exc

        try:
            return response.json()
        except ValueError as exc:
            raise ValueError(f"GET {response.url} returned invalid JSON: {exc}") from exc

    def post(self, path, json=None):
        response = requests.post(self.base_url + path, headers=self._headers(), json=json)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            raise requests.HTTPError(
                f"POST {response.url} failed with status {response.status_code}: {response.text}") from exc

        try:
            return response.json()
        except ValueError as exc:
            raise ValueError(f"POST {response.url} returned invalid JSON: {exc}") from exc