import time
import requests

for i in range(5):
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(i, resp.status_code)
    time.sleep(1)  # wait 1 sec between calls