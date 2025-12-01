import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(resp.json())