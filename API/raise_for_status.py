import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/100000")
try:
    resp.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
else:
    print("Success:", resp.json())