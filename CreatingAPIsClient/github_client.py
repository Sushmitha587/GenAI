import os
import requests

class GitHubClient:
    def __init__(self, token: str | None = None):
        self.base_url = "https://api.github.com"
        self.session = requests.Session()

        # read token from argument or environment variable
        if token is None:
            token = os.getenv("GITHUB_TOKEN")

        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json"
            })

    def get_user(self, username: str):
        # GET /users/{username}
        url = f"{self.base_url}/users/{username}"
        resp = self.session.get(url, timeout=5)
        resp.raise_for_status()
        return resp.json()

    def create_repo(self, name: str, private: bool = True):
        # POST /user/repos
        url = f"{self.base_url}/user/repos"
        payload = {"name": name, "private": private}
        resp = self.session.post(url, json=payload, timeout=5)
        resp.raise_for_status()
        return resp.json()