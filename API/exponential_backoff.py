import time
import requests

def safe_get(url, max_retries=3):
    for attempt in range(max_retries):
        resp = requests.get(url)
        if resp.status_code == 429:
            wait = 2 ** attempt       # 1s, 2s, 4s...
            print(f"Rate limited. Waiting {wait} seconds...")
            time.sleep(wait)
            continue
        return resp
    raise RuntimeError("Max retries reached")

resp = safe_get("https://api.github.com/users/octocat")
print(resp.status_code)