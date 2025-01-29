<div align="center">
    <img src="https://serancon.de/wp-content/uploads/2022/03/logo.png" alt="Logo" style="width:50%;">
</div>



<div align="center">
   
### 👋 Willkommen in meinem Shelly Repo!  

[![Website](https://img.shields.io/badge/Website-Visit-blue?style=for-the-badge)](https://serancon.de) [![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Individuum92)

</div>

Das Skript ist ein MQTT-Listener, der Daten (Temperatur, Luftfeuchtigkeit,- und Batterie Signalstärke) von Shelly-Sensoren (Shelly H&T Gen3 ) über MQTT empfängt, verarbeitet und in einer JSON-Datei speichert. Es sorgt dafür, dass die letzten bekannten Sensordaten nicht verloren gehen, falls ein neuer Wert fehlt. Die Daten werden anhand der MAC-Adresse bzw. Geräte-ID des jeweiligen Shelly-Sensors identifiziert.


![GitHub issues](https://img.shields.io/github/issues/Individuum92/check_mk)
 ![GitHub last commit](https://img.shields.io/github/last-commit/Individuum92/check_mk) ![GitHub repo size](https://img.shields.io/github/repo-size/Individuum92/check_mk)

<br>

## Sprachen und Technologien

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberry-pi&logoColor=white)

<br>

### Grundlegende Funktionen des Skripts

✔ Verbindet sich mit einem MQTT-Broker (standardmäßig localhost:1883)  
✔ Abonniert alle MQTT-Nachrichten vom Topic `shelly/#`    
✔ Extrahiert Sensordaten (Temperatur, Luftfeuchtigkeit, Batteriestatus, WLAN-Signalstärke)  
✔ Speichert Sensordaten in JSON-Dateien unter `/tmp/shelly_environment_<Raum>.json`  
✔ Stellt sicher, dass alte Werte erhalten bleiben, wenn ein Sensor einen Wert nicht sendet  

Stellt eine Verbindung zum MQTT-Broker (localhost:1883) her und abonniert das Topic `shelly/#`, um alle relevanten Shelly-Nachrichten zu empfangen empfängt alle Subtopics wie `shelly/device1/sensor`.
Ordnet MAC-Adressen von Shelly-Sensoren bestimmten Räumen zu, z. B. "e4b3232fe214" → "Büro".

<br>

### Relevante Sensordaten aus der JSON-Nachricht

Temperatur (tC)
Luftfeuchtigkeit (rh)
Batterieladestand (battery.percent)
WLAN-Signalstärke (wifi.rssi)

<br>

### Fehlende Werte aus vorherigen Messungen übernehmen

Falls ein Wert in der aktuellen Nachricht fehlt, wird der zuletzt gespeicherte Wert aus der entsprechenden JSON-Datei (/tmp/shelly_environment_<Raum>.json) verwendet.

<br>

### Als Service einrichten

Um den Broker als Dienst im Hintergrund laufen zu lassen, kann ein Dienst eingerichtet werden:
`nano /etc/systemd/system/shelly_mqtt.service`

```
[Unit]
Description=Shelly MQTT Listener
After=network.target

[Service]
ExecStart=/usr/bin/python3 /pfad/zum/skript/shelly_mqtt.py
WorkingDirectory=/
Restart=always
User=root
Group=root

[Install]
WantedBy=multi-user.target
```

Als Service aktivieren, sodass auch bei einem Neustart des Systems der Service automatisch startet.
```
sudo systemctl daemon-reload
sudo systemctl enable shelly_mqtt.service
sudo systemctl start shelly_mqtt.service
```

Falls du sehen möchtest, ob der Dienst läuft bzw. es Fehler gibt:
`sudo systemctl status shelly_mqtt.service`

<br>

### Inbetriebnahme auf einem Raspberry-Pi

Getestet und produktiv genommen wurde das Skript auf einem Raspi 5. Die sauberste Lösung ist, eine virtuelle Umgebung für das ausführen der Skriptes zu erstellen, um die notwendigen Voraussezungen nicht Systemweit zu installieren.  

🔹 Vorteil: Keine Konflikte mit systemweiten Python-Paketen  
🔹 Nachteil: Du musst die Umgebung jedes Mal aktivieren, bevor du dein Skript ausführst  


Das geht schnell und einfach wie folgt:

```
python3 -m venv ~/mqtt_env
source ~/mqtt_env/bin/activate
pip install paho-mqtt
```

<br>

**Eine kurze Erläuterung dazu:**

*python3 -m venv ~/mqtt_env*  
🔹 Erstellt eine virtuelle Python-Umgebung namens mqtt_env im Home-Verzeichnis ~/  
🔹 Eine virtuelle Umgebung (venv) isoliert Python-Pakete von der systemweiten Installation  
🔹 Dadurch werden Abhängigkeiten nur in dieser Umgebung installiert, ohne das System zu verändern  
🔹 Das Verzeichnis ~/mqtt_env/ enthält die isolierte Python-Installation  

*source ~/mqtt_env/bin/activate*  
🔹 Aktiviert die virtuelle Umgebung mqtt_env  
🔹 Danach nutzt das Terminal diese Umgebung für Python und pip, statt die systemweite Installation  
🔹 In der Eingabeaufforderung erscheint (mqtt_env), um anzuzeigen, dass die Umgebung aktiv ist  
🔹 Solange die Umgebung aktiv ist, wird python aus ~/mqtt_env/bin/python verwendet  

*pip install paho-mqtt*  
🔹 Installiert das Paket paho-mqtt nur in der virtuellen Umgebung  
🔹 paho-mqtt ist die Python-Bibliothek für die MQTT-Kommunikation  
🔹 Diese Installation betrifft nur ~/mqtt_env/, nicht das gesamte System  

Info: Um die Virtuelle Umgebung zu verlassen, einfach `deavtivate` in die Konsole eingeben. 

<br>

## Statistiken

[![GitHub stars](https://img.shields.io/github/stars/Individuum92/check_mk?style=for-the-badge)](https://github.com/Individuum92/check_mk/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Individuum92/check_mk?style=for-the-badge)](https://github.com/Individuum92/check_mk/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/Individuum92/check_mk?style=for-the-badge)](https://github.com/Individuum92/check_mk/watchers)


