import requests
from random import choice

# Circuit breaker state
FAILURES = 0
OPEN = False
THRESHOLD = 3  # Number of consecutive failures before opening the circuit

# Fake API simulator
def fake_api():
    # Randomly succeed or fail
    if choice([True, False, False]):  # 1/3 chance success, 2/3 fail
        return {"status": "ok", "data": "API response"}
    else:
        raise requests.exceptions.RequestException("Simulated API failure")

# Circuit breaker function
def call_partner_api():
    global FAILURES, OPEN

    if OPEN:
        raise RuntimeError("Circuit open - external API is down")

    try:
        resp = fake_api()  # Replace with requests.get("https://real-api.com") in real use
        FAILURES = 0       # Reset failures on success
        return resp
    except requests.exceptions.RequestException as e:
        FAILURES += 1
        if FAILURES >= THRESHOLD:
            OPEN = True
        raise e

# Test the circuit breaker
if __name__ == "__main__":
    for i in range(10):
        print(f"\nAttempt {i+1}:")
        try:
            result = call_partner_api()
            print("API Call Success:", result)
        except Exception as e:
            print("API Call Failed:", e)
        finally:
            print("Current Circuit State -> FAILURES:", FAILURES, "OPEN:", OPEN)