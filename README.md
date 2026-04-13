# Wettervorhersage Projekt

Dieses kleine Python-Projekt zeigt die aktuelle Wettervorhersage für mehrere Städte an.  
Die Daten werden von der OpenWeatherMap API abgerufen und in einer HTML-Tabelle angezeigt.

## Funktionsweise

- Der Benutzer gibt beliebige Städte in der Konsole ein.
- Das Skript erzeugt automatisch die Datei `wetter.html`.
- Wetter-Icons zeigen Sonne, Wolken, Regen, Schnee, Wind oder Sonne mit Wolken.
- Die Ausgabe erscheint sowohl in der Konsole als auch im Browser.

## Beispielhafte Ausgabe

**Konsole:**  
!\[Konsole](icons/ScreenKonsol.png)

**Browser:**  
!\[Browser](icons/ScreenBrowser.png)

## Verwendete Dateien

- `Wettervorhersage.py` – Hauptskript  
- `index.html` – HTML-Vorlage  
- `style.css` – Styling der Tabelle  
- Icons: `sun.png`, `cloud.png`, `rain.png`, `snow.png`, `wind.png`, `sun_cloud.png`  
- `wetter.html` – erzeugte HTML-Datei  

## Anleitung

1. Stelle sicher, dass alle Icons und die `index.html` im gleichen Ordner liegen.  
2. Starte das Skript:  
   ```bash
   python Wettervorhersage.py
Gib die gewünschten Städtenamen in der Konsole ein.
Die Ergebnisse werden in der Konsole angezeigt und die HTML-Datei wetter.html automatisch geöffnet.








