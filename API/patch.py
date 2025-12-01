import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"title": "Only Title Updated"}

resp = requests.patch(url, json=payload)
print(resp.status_code)
print(resp.json())