import requests

try:
    r = requests.get("https://httpbin.org/delay/3", timeout=2)
    print("Success:", r.status_code)
except requests.exceptions.Timeout:
    print("Request took too long!")