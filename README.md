# REPO UNDER CONSTRUCTION

<div align="center">
    <img src="https://serancon.de/wp-content/uploads/2022/03/logo.png" alt="Logo" style="width:50%;">
</div>



<div align="center">
   
### 👋 Willkommen in meinem Shelly Repo!  

[![Website](https://img.shields.io/badge/Website-Visit-blue?style=for-the-badge)](https://serancon.de) [![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Individuum92)

</div>

Dieses Python-Skript empfängt Umweltdaten (Temperatur, Luftfeuchtigkeit, -und Batterie Signalstärke) von Shelly-Sensoren über MQTT und speichert die aktuellen Werte als JSON-Dateien im Verzeichnis /tmp/. Die Daten werden anhand der MAC-Adresse des jeweiligen Shelly-Sensors identifiziert und einem benutzerfreundlichen Namen (z. B. „Büro“, „Wohnzimmer“) zugeordnet.

![GitHub issues](https://img.shields.io/github/issues/Individuum92/check_mk)
 ![GitHub last commit](https://img.shields.io/github/last-commit/Individuum92/check_mk) ![GitHub repo size](https://img.shields.io/github/repo-size/Individuum92/check_mk)

<br>

## Sprachen und Technologien

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberry-pi&logoColor=white)

<br>

## Hauptfunktionen
#### Verbindung zum MQTT-Broker aufbauen

Stellt eine Verbindung zum MQTT-Broker (localhost:1883) her.
Abonniert das Topic shelly/#, um alle relevanten Shelly-Nachrichten zu empfangen.

#### Empfangene MQTT-Nachrichten verarbeiten

Liest und dekodiert die JSON-Daten der Shelly-Sensoren.
Extrahiert die MAC-Adresse aus der Nachricht.
Falls die MAC-Adresse in der bekannten Mapping-Liste (SHELLY_NAME_MAPPING) enthalten ist, wird der Sensor identifiziert.

#### Relevante Sensordaten aus der JSON-Nachricht extrahieren

Temperatur (tC)
Luftfeuchtigkeit (rh)
Batterieladestand (battery.percent)
WLAN-Signalstärke (wifi.rssi)

#### Fehlende Werte aus vorherigen Messungen übernehmen

Falls ein Wert in der aktuellen Nachricht fehlt, wird der zuletzt gespeicherte Wert aus der entsprechenden JSON-Datei (/tmp/shelly_environment_<Raum>.json) verwendet.

#### Daten als JSON speichern

Die Messwerte und der aktuelle Zeitstempel (timestamp) werden in einer JSON-Datei abgelegt, um spätere Abfragen zu ermöglichen.

#### Dauerhafte MQTT-Schleife zur Verarbeitung neuer Nachrichten

Das Skript bleibt kontinuierlich aktiv und verarbeitet alle eintreffenden MQTT-Nachrichten.

<br>

## Statistiken

[![GitHub stars](https://img.shields.io/github/stars/Individuum92/check_mk?style=for-the-badge)](https://github.com/Individuum92/check_mk/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Individuum92/check_mk?style=for-the-badge)](https://github.com/Individuum92/check_mk/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/Individuum92/check_mk?style=for-the-badge)](https://github.com/Individuum92/check_mk/watchers)

<br>

## ToDo

- [X] Ordnerstruktur überarbeiten, sodass standardisierte Parameter bestehen (für Logs, Arbeitsdateien und etc.)
- [ ] Eindeutigkeit in die Servicenamen einbinden (Serancon {SERVICE NAME}), um z.B. Gruppierungen vornehmen zu können
- [X] Extensions an alle Skripte hängen sodass erkennbar ist, in welcher Sprache das Skript vorliegt
- [ ] Umlaute anpassen (Ä,Ö,Ü)
- [ ] Update Automatismus der README-Datei einbinden
- [ ] Die jeweiligen Voraussetzungen der Skripte beschreiben
- [ ] DE / EN Versionen

