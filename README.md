# REPO UNDER CONSTRUCTION

<div align="center">
    <img src="https://serancon.de/wp-content/uploads/2022/03/logo.png" alt="Logo" style="width:50%;">
</div>



<div align="center">
   
### 👋 Willkommen in meinem eigenen Check_MK Repo!  

[![Website](https://img.shields.io/badge/Website-Visit-blue?style=for-the-badge)](https://serancon.de) [![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Individuum92)

</div>

Aus meiner eigenen Erfahrung und der Betreuung von Kunden im Bereich Monitoring heraus habe ich beschlossen, eigene Checks zu entwickeln und hier öffentlich bereitzustellen. Mein Ziel ist es, die Skripte kontinuierlich zu aktualisieren und zu verbessern.

Falls Sie Anregungen oder spezielle Anforderungen haben, lassen Sie es mich wissen. Bei Problemen oder Fehlern können Sie gerne die Issue-Funktion nutzen.

![GitHub issues](https://img.shields.io/github/issues/Individuum92/check_mk)
 ![GitHub last commit](https://img.shields.io/github/last-commit/Individuum92/check_mk) ![GitHub repo size](https://img.shields.io/github/repo-size/Individuum92/check_mk)

## Warum dieses Repository?

CheckMK ist ein mächtiges Tool zur Überwachung von Systemen. Dieses Repository stellt zusätzliche Skripte zur Automatisierung bereit, um:  
✔️ Skripte automatisieren wiederkehrende Aufgaben und reduzieren den Verwaltungsaufwand in CheckMK  
✔️ Zentrale Bereitstellung und Verwaltung aller Skripte statt manueller Updates auf mehreren Servern  
✔️ Der GitHub-Downloader hält Skripte automatisch aktuell – ohne manuelles Kopieren  
✔️ Open Source, gut dokumentiert und leicht anpassbar – ideal für Anfänger und Profis  
✔️ Learning by doing und Hilfe zur Selbsthilfe

<!--
<br>
<details>
  <summary>📚 Inhaltsverzeichnis</summary>

- [Sprachen und Technologien](#Sprachen-und-Technologien)
- [Skript-Downloader](#Skript-Downloader)
- [Installation & Nutzung](#installation--nutzung)
- [Verfügbare Skripte](#verfügbare-skripte)
- [Statistiken](#statistiken)
- [ToDo](#todo)

</details>
-->

<br>

## Sprachen und Technologien

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberry-pi&logoColor=white)

<br>

## Skript-Downloader

Der Skript-Downloader ermöglicht es, Skripte aus dem GitHub-Repository *check_mk* einfach auszuwählen, herunterzuladen und ausführbar zu machen. Die Skripte werden dabei automatisch in den richtigen Ordner verschoben und können bearbeitet werden.  
Das Skript ruft die Liste der Dateien aus dem Repository ab. Dem Benutzer wird ein interaktives Menü zur Auswahl der Skripte angezeigt.  
**Ort der Skripte:** `/usr/etc/check_mk/local`

<br>

### Installation & Nutzung

#### Ordnerstruktur anlegen

Voraussetzungen für die Nutzung der Skripte ist, dass folgende Ordnerstruktur besteht. Diese wird automatisch bei Ausführung des Skript-Downloader's angelegt:
- /etc/serancon
- /var/log/serancon
- /tmp/serancon

#### Github-Downloader herunterladen
   ```bash
   wget https://raw.githubusercontent.com/Individuum92/check_mk/main/github_downloader.sh
   chmod +x github_downloader.sh
   ```

#### Skript ausführen
   ```bash
   ./github_downloader.sh
   ```



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

