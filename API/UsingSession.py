import requests

session = requests.Session()
session.headers.update({"Authorization": "Bearer TOKEN"})

# First call
r1 = session.get("https://jsonplaceholder.typicode.com/posts/1")
# Second call with same headers + connection reused
r2 = session.get("https://jsonplaceholder.typicode.com/posts/2")

print(r1.status_code, r2.status_code)