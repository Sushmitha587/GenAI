'''import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")  # secure
print(resp.status_code)'''


import requests

# NOT recommended for production
resp = requests.get("https://expired.badssl.com/", verify=False)
print(resp.status_code)