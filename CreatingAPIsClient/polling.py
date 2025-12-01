import time
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"  # Example API

def poll_api(interval=5, max_attempts=5):
    for attempt in range(max_attempts):
        print(f"Polling attempt {attempt+1}...")
        try:
            resp = requests.get(API_URL, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            print("Received data:", data)
        except requests.RequestException as e:
            print("Error:", e)
        
        time.sleep(interval)  # wait before next poll

if __name__ == "__main__":
    poll_api()
