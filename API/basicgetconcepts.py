import requests

base_url = "https://jsonplaceholder.typicode.com"
endpoint = "/posts"
url = base_url + endpoint

params = {"userId": 1}                    # query params
headers = {"Accept": "application/json"}  # headers

response = requests.get(url, params=params, headers=headers)

print("Final URL:", response.url)
print("Status:", response.status_code)
print("Headers:", response.headers["Content-Type"])
print("Body sample:", response.json()[0])