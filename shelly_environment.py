#!/usr/bin/env python3
import json
import os
import glob
from datetime import datetime

# Konfiguration: Welche Werte sollen erfasst werden?
ENABLE_TEMPERATURE = True       # Temperatur erfassen? (True/False)
ENABLE_HUMIDITY = True          # Luftfeuchtigkeit erfassen? (True/False)
ENABLE_BATTERY = True           # Batteriestatus erfassen? (True/False)

# Datenpfad
DATA_PATH = "/tmp/shelly_environment_*.json"
PREFIX_ENABLED = 1  # 1 = "Serancon: " wird vorangestellt, 0 = deaktiviert

# Schwellenwerte
TEMP_WARN = 30
TEMP_CRIT = 40
HUMIDITY_WARN = 60
HUMIDITY_CRIT = 80
BATTERY_WARN = 20
BATTERY_CRIT = 10

# Funktion zur Erstellung der Performance-Daten
def create_perfdata(name, value, warn, crit, min_val=None, max_val=None):
    if value is None:
        return None
    return f'{name}={value};{warn};{crit};{min_val if min_val is not None else ""};{max_val if max_val is not None else ""}'

# Alle vorhandenen Shelly JSON-Dateien abrufen
shelly_files = glob.glob(DATA_PATH)
output = []

if not shelly_files:
    print('2 "Serancon: Shelly Monitoring" - No Shelly data found')
    exit(2)

for file in shelly_files:
    try:
        with open(file, "r") as f:
            data = json.load(f)

        shelly_id = os.path.basename(file).replace("shelly_environment_", "").replace(".json", "")
        timestamp = data.get("timestamp")
        temperature = data.get("temperature")
        humidity = data.get("humidity")
        battery = data.get("battery")

        if timestamp:
            time_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

            # Service-Name für das Gerät
            service_name = f"Serancon: Shelly {shelly_id}" if PREFIX_ENABLED else f"Shelly {shelly_id}"

            # Performance-Daten mit `|` trennen
            perfdata_list = []
            if ENABLE_HUMIDITY:
                humidity_perf = create_perfdata("humidity", humidity, HUMIDITY_WARN, HUMIDITY_CRIT, 10, 100)
                if humidity_perf:
                    perfdata_list.append(humidity_perf)

            if ENABLE_BATTERY:
                battery_perf = create_perfdata("battery", battery, BATTERY_WARN, BATTERY_CRIT, 0, 100)
                if battery_perf:
                    perfdata_list.append(battery_perf)
            if ENABLE_TEMPERATURE:
                temp_perf = create_perfdata("temperature", temperature, TEMP_WARN, TEMP_CRIT, -10, 60)
                if temp_perf:
                    perfdata_list.append(temp_perf)

            # Wenn keine Werte verfügbar sind, nicht ausgeben
            if perfdata_list:
                perfdata_str = "|".join(perfdata_list)  # **Hier die Pipe (`|`) nutzen**
                output.append(f'0 "{service_name}" {perfdata_str} '
                              f'Temperature: {temperature if temperature is not None else "N/A"}°C, '
                              f'Humidity: {humidity if humidity is not None else "N/A"}%, '
                              f'Battery: {battery if battery is not None else "N/A"}% (measured at: {time_str})')

    except json.JSONDecodeError:
        print(f'2 "Serancon: Shelly {shelly_id} Monitoring" - Data file contains invalid JSON')
    except Exception as e:
        print(f'2 "Serancon: Shelly {shelly_id} Monitoring" - Error reading data file: {e}')

if output:
    print("\n".join(output))
else:
    print('2 "Serancon: Shelly Monitoring" - No valid data found')
