from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/proxy")
def proxy():
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=2)
        r.raise_for_status()
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Upstream timeout")
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="Upstream error")
    return r.json()