import requests

# Sample "order IDs"
order_ids = [1, 2, 3]

# Using JSONPlaceholder to simulate bulk order details
resp = requests.post(
    "https://jsonplaceholder.typicode.com/posts",  # POST endpoint
    json={"ids": order_ids},  # sending data in JSON
    timeout=5
)

# Convert response to Python object
details = resp.json()

# Print response
print("Response from server:")
print(details)
