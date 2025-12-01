import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}

print("→ Sending GET", url, "with params", params)
resp = requests.get(url, params=params)
print("← Status:", resp.status_code)
print("← First item:", resp.json()[0])