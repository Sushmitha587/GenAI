import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "New Post", "body": "Hello API", "userId": 1}

resp = requests.post(url, json=payload)
print(resp.status_code)    # 201 Created (in real APIs)
print(resp.json())