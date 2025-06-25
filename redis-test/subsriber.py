import redis
import os

# Connect to Redis (default localhost:6379)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

CHANNEL = "my_channel"

pubsub = r.pubsub()
pubsub.subscribe(CHANNEL)

print(f"Listening for messages on channel: {CHANNEL}")
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Received: {message['data']}")