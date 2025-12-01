import requests

# --- STEP 1: READ API KEY FROM config.txt ---
API_KEY = None
with open("config.txt", "r") as f:
    for line in f:
        if line.startswith("API_KEY"):
            API_KEY = line.split("=")[1].strip()

# --- Check if key loaded ---
if not API_KEY:
    raise ValueError("API key not found in config.txt")

# --- STEP 2: CALL OPENWEATHERMAP API ---
url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "London",
    "appid": API_KEY,
    "units": "metric"
}

resp = requests.get(url, params=params)

print("Status code:", resp.status_code)

if resp.status_code == 200:
    print("Weather data:", resp.json())
else:
    print("Error:", resp.text)
