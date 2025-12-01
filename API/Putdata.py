import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"id": 1, "title": "Updated", "body": "New body", "userId": 1}

resp = requests.put(url, json=payload)
print(resp.status_code)
print(resp.json())