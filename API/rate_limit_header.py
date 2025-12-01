import requests

resp = requests.get("https://api.github.com/users/octocat")
print("Limit:", resp.headers.get("X-RateLimit-Limit"))
print("Remaining:", resp.headers.get("X-RateLimit-Remaining"))