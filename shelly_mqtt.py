#!/usr/bin/env python3
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import paho.mqtt.client as mqtt
import json
import time
import os

# MQTT-Broker-Konfiguration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "shelly/#"

# Mapping von Shelly MAC-Adressen zu Namen
SHELLY_NAME_MAPPING = {
    "e4b3232fe214": "Büro",
    "8cbfeaa5ed1c": "Wohnzimmer",
    "8cbfeaa542d8": "Badezimmer",
    "e4b32331b14c": "Schlafzimmer",
    "34b7da8cfe90": "Balkon"
}

# Funktion zum Laden der letzten bekannten Werte
def load_last_values(data_file):
    if os.path.exists(data_file):
        try:
            with open(data_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"temperature": None, "humidity": None, "battery": None, "wifi_signal": None, "timestamp": None}
    return {"temperature": None, "humidity": None, "battery": None, "wifi_signal": None, "timestamp": None}

# Funktion zur Suche nach Sensorwerten
def find_sensor_data(data):
    result = {"temperature": None, "humidity": None, "battery": None, "wifi_signal": None}

    if isinstance(data, dict):
        if "tC" in data:
            result["temperature"] = data["tC"]
        if "rh" in data:
            result["humidity"] = data["rh"]
        if "battery" in data and isinstance(data["battery"], dict):
            result["battery"] = data["battery"].get("percent")
        if "wifi" in data and isinstance(data["wifi"], dict):
            result["wifi_signal"] = data["wifi"].get("rssi")

        for key, value in data.items():
            sub_result = find_sensor_data(value)
            for k in result.keys():
                if sub_result[k] is not None:
                    result[k] = sub_result[k]

    elif isinstance(data, list):
        for item in data:
            sub_result = find_sensor_data(item)
            for k in result.keys():
                if sub_result[k] is not None:
                    result[k] = sub_result[k]

    return result

# Funktion zur MAC-Adressen-Erkennung
def extract_mac_address(payload):
    if isinstance(payload, dict):
        if "mac" in payload:
            return payload["mac"].lower()
        if "sys" in payload and "mac" in payload["sys"]:
            return payload["sys"]["mac"].lower()
        if "params" in payload:
            if isinstance(payload["params"], dict) and "sys" in payload["params"] and "mac" in payload["params"]["sys"]:
                return payload["params"]["sys"]["mac"].lower()
    return None

# Callback für empfangene MQTT-Nachrichten
def on_message(client, userdata, msg):
    try:
        payload_raw = msg.payload.decode("utf-8")
        payload = json.loads(payload_raw)
        mac_address = extract_mac_address(payload)

        if not mac_address or mac_address not in SHELLY_NAME_MAPPING:
            return

        shelly_name = SHELLY_NAME_MAPPING.get(mac_address)
        data_file = f"/tmp/shelly_environment_{shelly_name}.json"
        last_values = load_last_values(data_file)
        sensor_data = find_sensor_data(payload)

        # Falls keine neuen Werte gefunden wurden, nimm die letzten bekannten Werte
        if sensor_data["temperature"] is None:
            sensor_data["temperature"] = last_values["temperature"]
        if sensor_data["humidity"] is None:
            sensor_data["humidity"] = last_values["humidity"]
        if sensor_data["battery"] is None:
            sensor_data["battery"] = last_values["battery"]
        if sensor_data["wifi_signal"] is None:
            sensor_data["wifi_signal"] = last_values["wifi_signal"]

        timestamp = int(time.time())

        try:
            with open(data_file, "w") as f:
                json.dump({"timestamp": timestamp, **sensor_data}, f)
        except Exception as e:
            pass

    except json.JSONDecodeError:
        pass
    except Exception:
        pass

# MQTT-Client initialisieren
client = mqtt.Client(client_id="", protocol=mqtt.MQTTv5)
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC)

client.loop_forever()
