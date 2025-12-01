'''import requests

# Fixed with real URL
resp = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"completed": "false"},  # using a filter that exists
)
orders = resp.json()

# Safely print info
print("Filtered orders count:", len(orders))
if orders:
    print("Sample order:", orders[0])
else:
    print("No orders found")'''
    