import requests

url = "https://httpbin.org/post"
data = {"username": "gopi", "password": "secret"}
resp = requests.post(url, data=data)
print(resp.json()["form"])