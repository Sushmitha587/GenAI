from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook_receiver(request: Request):
    data = await request.json()
    print("Webhook Received:", data)
    return {"status": "success"}
