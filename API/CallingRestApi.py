import requests

# Get all books
resp = requests.get("https://jsonplaceholder.typicode.com/posts")
print(resp.status_code)
print(resp.json())

# Add a new book
new_book = {"title": "LangChain for Beginners", "author": "ItTechGenie"}
resp = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_book)
print("Created:", resp.status_code, resp.json())
