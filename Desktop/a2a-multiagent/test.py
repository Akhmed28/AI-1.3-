import requests

# Simulate starting the flow
a2a_message = {
    "sender": "user",
    "receiver": "agent1",
    "message": "Hello from test!"
}

response = requests.post("http://localhost:8000/agent1", json=a2a_message)

print("Final Response:", response.json())
