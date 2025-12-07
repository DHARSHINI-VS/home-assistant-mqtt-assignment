# Home Assistant MQTT Sensor Integration

## Student Information
- **Name:** DHARSHINI VS
- **Register Number:** 42110287
- **MQTT Topic:** home/dharshini-2025/sensor

## Project Description
This project demonstrates integration of MQTT sensors with Home Assistant using Python and Mosquitto broker.

## Sensors Implemented
1. **Temperature Sensor** - Publishes temperature data (25°C)
2. **Humidity Sensor** - Publishes humidity data (60%)
3. **Light Sensor** - Publishes ambient light data (300 lux)

## Technologies Used
- Home Assistant
- Mosquitto MQTT Broker
- Python with paho-mqtt library
- MQTT Auto-Discovery

## Setup Instructions

### Prerequisites
- Home Assistant installed
- Mosquitto MQTT Broker installed and running
- Python with paho-mqtt library (`pip install paho-mqtt`)

### How to Run
1. Ensure Mosquitto broker is running
2. Run the Python script:
```bash
   python mqtt_sensors.py
```
3. Open Home Assistant and navigate to Settings → Devices & Services → MQTT
4. The sensors will auto-discover and appear under "DHARSHINI VS Sensors"

## MQTT Topic Structure
- Base topic: `home/dharshini-2025/sensor`
- Temperature: `home/dharshini-2025/sensor/temperature`
- Humidity: `home/dharshini-2025/sensor/humidity`
- Light: `home/dharshini-2025/sensor/light`

## Features
- Auto-discovery configuration for Home Assistant
- Real-time sensor data publishing every 5 seconds
- Clean and documented Python code
- Proper device grouping in Home Assistant

## Assignment Requirements Met
✅ Home Assistant installed  
✅ Mosquitto MQTT Broker installed  
✅ Python script with required variables (student_name, unique_id, topic)  
✅ Three sensors (temperature, humidity, light)  
✅ Live data display in Home Assistant  
✅ Unique MQTT topic structure
