Wettervorhersage mit OpenWeather API

Für dieses Projekt wird die OpenWeather API verwendet, um aktuelle Wetterdaten abzurufen.

API: OpenWeather

Beschreibung: Ein Python-Programm, das das aktuelle Wetter für ausgewählte Städte abruft und sowohl im Terminal als auch als HTML-Tabelle im Browser darstellt.

Aufgabe: Wetterinformationen wie Temperatur, gefühlte Temperatur und Wetterbeschreibung für die Städte Mannheim, Berlin, Sevastopol und Kiev abrufen.

Frameworks / Libraries:

Python 3.x

requests – für HTTP-Anfragen an die OpenWeather API

datetime – zur Anzeige der aktuellen Uhrzeit

HTML / CSS – für die Darstellung der Wetterdaten in Tabellenform

Kurze Anleitung zum Starten des Programms:

Python 3.x installiert

PowerShell oder Terminal öffnen

In den Projektordner wetter/ navigieren

Bibliothek requests installieren, falls noch nicht geschehen:

    pip install requests


Programm starten:

    python Wettervorhersage.py


Die Wetterinformationen werden im Terminal angezeigt und zusätzlich die Datei wetter.html automatisch erstellt.

Die HTML-Datei kann im Browser geöffnet werden, um die Wetterdaten in einer Tabelle zu sehen.

Projektdateien:

Wettervorhersage.py – Python-Skript, das die API abfragt und HTML generiert

 index.html – HTML-Vorlage für die Tabelle

 style.css – CSS-Datei für die Darstellung der Tabelle

 wetter.html – automatisch generierte HTML-Datei

 README.md – kurze Projektbeschreibung für GitHub

 Projektdokumentation.md – ausführliche Projektbeschreibung

Beispielhafte Ausgabe im Terminal:
Mannheim (19.01.2026 10:17) 1.93°C -0.28°C Bedeckt
Berlin (19.01.2026 10:17) -0.63°C -5.79°C Klarer Himmel
Sevastopol (19.01.2026 10:17) -1.11°C -4.05°C Mäßig bewölkt
Kiev (19.01.2026 10:17) -9.49°C -9.49°C Mäßig bewölkt

Beispielhafte Anzeige in HTML:
Die gleiche Tabelle wie oben, aber in einem Browser mit CSS formatiert.
