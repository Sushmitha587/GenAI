
import requests
_cache = {}

def get_product(product_id: str):
    if product_id in _cache:
        print("Using cache for", product_id)
        return _cache[product_id]

    resp = requests.get(f"https://jsonplaceholder.typicode.com/posts/{product_id}")
    resp.raise_for_status()
    data = resp.json()
    _cache[product_id] = data
    return data

# First request (fetches from server)
product1 = get_product("1")
print(product1)

# Second request (uses cache)
product1_again = get_product("1")
print(product1_again)
