import requests
from requests.exceptions import RequestException, Timeout

def fetch_with_handling(url):
    try:
        resp = requests.get(url, timeout=3)
        resp.raise_for_status()
    except Timeout:
        print("⏰ Timeout while calling:", url)
        return None
    except RequestException as e:
        print("❌ Request failed:", e)
        return None
    else:
        return resp.json()

data = fetch_with_handling("https://jsonplaceholder.typicode.com/posts/1")
print("Data:", data)