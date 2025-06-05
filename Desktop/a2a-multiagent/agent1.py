from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.post("/agent1")
async def process_request(request: Request):
    data = await request.json()

    print("Agent1 received message:", data)

    # Example processing: just uppercase the incoming message
    message = data.get("message", "")
    response = f"LangChain agent processed: {message.upper()}"

    # Send the processed response to agent2’s API endpoint
    a2a_payload = {
        "sender": "agent1",
        "receiver": "agent2",
        "message": response
    }

    r = requests.post("http://localhost:8001/agent2", json=a2a_payload)

    return {"status": "sent to agent2", "agent2_response": r.json()}
