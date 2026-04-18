
import paho.mqtt.client as mqtt
import json
import time
import random

MQTT_BROKER = "broker.emqx.io"
MQTT_TOPIC = "python/iot/dashboard/demo"

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)
print(f"Publishing to {MQTT_TOPIC}...")

try:
    while True:
        data = {
            "Temperature": round(random.uniform(22.0, 28.0), 1),
            "Humidity": round(random.uniform(45.0, 55.0), 1),
            "Signal": random.randint(-70, -40)
        }
        client.publish(MQTT_TOPIC, json.dumps(data))
        print(f"Sent: {data}")
        time.sleep(3)
except KeyboardInterrupt:
    pass
