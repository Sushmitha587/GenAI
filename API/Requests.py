# requests
import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("requests:", r.status_code)

# httpx (sync mode)
import httpx
r2 = httpx.get("https://jsonplaceholder.typicode.com/posts/1")
print("httpx:", r2.status_code)