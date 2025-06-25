from fastapi import FastAPI, Request
import redis
import os
from pydantic import BaseModel

app = FastAPI()

# Connect to Redis (default localhost:6379)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

CHANNEL = "my_channel"

class Message(BaseModel):
    message: str
@app.post("/publish")
def publish_message(data: Message):
    r.publish(CHANNEL, data.message)
    return {"status": "Message published", "channel": CHANNEL, "message": data.message}