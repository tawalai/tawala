class AuthManager:
    def __init__(self, http):
        self.http = http
        self.token = None

    def authenticate(self, api_key):
        res = self.http.post("/auth/exchange", json={"api_key": api_key})
        self.token = res["access_token"]