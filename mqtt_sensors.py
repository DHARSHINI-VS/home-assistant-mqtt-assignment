import paho.mqtt.client as mqtt
import json
import time

student_name = "DHARSHINI VS"
unique_id = "42110287"
topic_base = "home/dharshini-2025/sensor"

broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port)

temp_config = {
    "name": "Temperature Sensor",
    "state_topic": f"{topic_base}/temperature",
    "unit_of_measurement": "°C",
    "unique_id": f"{unique_id}_temp",
    "device": {
        "identifiers": [f"{unique_id}"],
        "name": f"{student_name} Sensors",
        "model": "Virtual Sensor",
        "manufacturer": "Student Project"
    }
}

humidity_config = {
    "name": "Humidity Sensor",
    "state_topic": f"{topic_base}/humidity",
    "unit_of_measurement": "%",
    "unique_id": f"{unique_id}_humidity",
    "device": {
        "identifiers": [f"{unique_id}"],
        "name": f"{student_name} Sensors",
        "model": "Virtual Sensor",
        "manufacturer": "Student Project"
    }
}

light_config = {
    "name": "Light Sensor",
    "state_topic": f"{topic_base}/light",
    "unit_of_measurement": "lux",
    "unique_id": f"{unique_id}_light",
    "device": {
        "identifiers": [f"{unique_id}"],
        "name": f"{student_name} Sensors",
        "model": "Virtual Sensor",
        "manufacturer": "Student Project"
    }
}

client.publish(
    f"homeassistant/sensor/{unique_id}_temp/config",
    json.dumps(temp_config),
    retain=True
)
client.publish(
    f"homeassistant/sensor/{unique_id}_humidity/config",
    json.dumps(humidity_config),
    retain=True
)
client.publish(
    f"homeassistant/sensor/{unique_id}_light/config",
    json.dumps(light_config),
    retain=True
)

print("Auto-discovery messages sent!")
print(f"Student: {student_name}")
print(f"Register Number: {unique_id}")
print(f"Publishing to: {topic_base}")

try:
    while True:
        client.publish(f"{topic_base}/temperature", "25")
        client.publish(f"{topic_base}/humidity", "60")
        client.publish(f"{topic_base}/light", "300")
        
        print(f"Published: Temperature=25°C, Humidity=60%, Light=300lux")
        time.sleep(5)
        
except KeyboardInterrupt:
    print("\nStopping...")
    client.disconnect()
