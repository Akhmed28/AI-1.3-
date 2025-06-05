from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/agent2")
async def receive_message(request: Request):
    data = await request.json()

    print("Agent2 received message:", data)

    # Simulate LlamaIndex-style processing
    msg = data.get("message", "")
    response = {
        "agent": "agent2",
        "summary": f"Summarized: {msg[:30]}..."  # fake summary
    }

    return response
