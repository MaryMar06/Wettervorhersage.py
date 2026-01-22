<<<<<<< HEAD
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
=======
Wettervorhersage Projekt – Projektdokumentation

1\. Projektname



Wettervorhersage



2\. Ziel des Projekts



Das Ziel des Projekts ist es, die aktuelle Wettervorhersage für eine beliebige Stadt anzuzeigen.



Die Daten werden von der OpenWeatherMap API abgerufen.



Die Ausgabe erfolgt sowohl in der Konsole als auch in einer HTML-Tabelle im Browser.



Wetter-Icons zeigen Sonne, Wolken, Regen, Schnee, Wind oder Sonne+Wolken an.



3\. Verwendete Dateien

Datei	Beschreibung

Wettervorhersage.py	Hauptskript, das Wetterdaten abruft und HTML generiert

index.html	Vorlage für die HTML-Tabelle

style.css	Styling für die Tabelle und Icons

sun.png, cloud.png, rain.png, snow.png, wind.png, sun\_cloud.png	Wetter-Icons

wetter.html	Vom Skript erzeugte HTML-Datei

screenshots/	Ordner für Beispiel-Screenshots (optional)

4\. Funktionsweise



Städte auswählen:



Der Nutzer kann die Städte direkt in der Konsole eingeben.



Alternativ können standardmäßig gespeicherte Städte im Skript verwendet werden.



Wetterdaten abrufen:



Das Skript nutzt die OpenWeatherMap API über HTTP-Anfragen (requests).



Temperatur, gefühlte Temperatur, Beschreibung der Wetterlage werden ausgelesen.



Icon auswählen:



Je nach Wetterbeschreibung wird ein passendes Icon gewählt (z. B. sun.png für Klarer Himmel).



HTML generieren:



Die Wetterdaten werden in die Vorlage index.html eingefügt.



Ergebnis wird in wetter.html gespeichert.



Ergebnis anzeigen:



Konsolenausgabe zeigt die aktuellen Werte der gewählten Städte.



Browser öffnet automatisch die Datei wetter.html.



5\. Benutzeranleitung



Stelle sicher, dass alle Dateien (Wettervorhersage.py, index.html, style.css, Icons) im selben Ordner liegen.



Starte die Konsole (PowerShell oder Terminal) im Projektordner.



Führe das Skript aus:



python Wettervorhersage.py





Gib, falls gewünscht, eine Stadt ein, um deren Wetter zu sehen.



Die HTML-Datei wetter.html öffnet sich automatisch im Browser.



6\. Screenshots (optional)



Konsole: zeigt die Ausgabe der Wetterwerte.



Browser: zeigt die Wetter-Tabelle mit Icons.









7\. Technische Hinweise



Programmiersprache: Python 3.x



Bibliotheken: requests, datetime, webbrowser



Wetter-API: OpenWeatherMap (API-Key erforderlich)



HTML/CSS für Darstellung der Tabelle und Icons.

>>>>>>> 628df69 (Dokumentation aktualisiert und Fehler behoben)
