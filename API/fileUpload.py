import requests

url = "https://httpbin.org/post"   # demo endpoint
files = {"file": ("example.txt", b"Hello from ItTechGenie!")}
resp = requests.post(url, files=files)
print(resp.json()["files"])