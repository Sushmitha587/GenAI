import concurrent.futures
import requests

# Function to fetch JSON data safely
def fetch(url: str):
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()  # raises exception if HTTP error
    return resp.json()       # return parsed JSON directly

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

# Use ThreadPoolExecutor to fetch concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
    results = list(ex.map(fetch, urls))

# Print results
for r in results:
    print("Status: 200", "| ID:", r["id"], "| Title:", r["title"])
