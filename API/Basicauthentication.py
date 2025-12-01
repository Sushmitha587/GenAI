import requests

url = "https://httpbin.org/basic-auth/user/passwod"
resp = requests.get(url, auth=("user", "passwod"))

print("Status:", resp.status_code)

if resp.status_code == 200:
    print("Response JSON:", resp.json())
else:
    print("Error Response:", resp.text)
