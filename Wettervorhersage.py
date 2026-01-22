import os
import requests
from datetime import datetime
import webbrowser

# Pfad überprüfen
print("Python sucht index.html hier:", os.path.abspath('index.html'))
print("Inhalt des Verzeichnisses:")
print(os.listdir())

# API-Schlüssel
api_schluessel = '972aafaa3761633381bef65cd97bfeb4'

# Benutzer gibt Städte ein
eingabe = input("Gib die Städte ein, getrennt durch Komma: ")
staedte = [stadt.strip() for stadt in eingabe.split(",")]

# HTML-Vorlage lesen
with open('index.html', 'r', encoding='utf-8') as datei:
    html_inhalt = datei.read()

insert_marker = '<!-- Python wird hier die Daten einfügen -->'
rows = ''

# Icons für Wetter
icons = {
    'sun': 'icons/sun.png',
    'sun_cloud': 'icons/sun_cloud.png',
    'cloud': 'icons/cloud.png',
    'rain': 'icons/rain.png',
    'snow': 'icons/snow.png',
    'wind': 'icons/wind.png'
}

for stadt in staedte:
    # API-Abfrage
    url = f'https://api.openweathermap.org/data/2.5/weather?q={stadt}&units=metric&lang=de&appid={api_schluessel}'
    antwort = requests.get(url)
    daten = antwort.json()
    zeit = datetime.now().strftime('%d.%m.%Y %H:%M')

    if 'main' in daten:
        temperatur = daten['main']['temp']
        gefuehlt = daten['main']['feels_like']
        beschreibung = daten['weather'][0]['description'].lower()  # alles klein

        # Icon wählen
        if 'klar' in beschreibung or 'heiter' in beschreibung:
            icon = icons['sun']
        elif 'sonne' in beschreibung and ('wolken' in beschreibung or 'bewölkt' in beschreibung):
            icon = icons['sun_cloud']
        elif 'wolken' in beschreibung or 'bewölkt' in beschreibung or 'trüb' in beschreibung:
            icon = icons['cloud']
        elif 'regen' in beschreibung or 'schauer' in beschreibung:
            icon = icons['rain']
        elif 'schnee' in beschreibung or 'snow' in beschreibung:
            icon = icons['snow']
        elif 'wind' in beschreibung or 'sturm' in beschreibung:
            icon = icons['wind']
        else:
            icon = icons['cloud']

        # Ausgabe in Konsole
        print(f'{stadt} ({zeit}): {temperatur}°C, gefühlt {gefuehlt}°C, {beschreibung}')

        # Zeile für HTML erstellen
        rows += f"""
        <tr>
            <td>{stadt} ({zeit})</td>
            <td><img src="{icon}" class="icon"> {temperatur}°C</td>
            <td>{gefuehlt}°C</td>
            <td>{beschreibung}</td>
        </tr>
        """
    else:
        rows += f"""
        <tr>
            <td>{stadt}</td>
            <td colspan="3">Fehler: Stadt nicht gefunden</td>
        </tr>
        """

# HTML aktualisieren
html_inhalt = html_inhalt.replace(insert_marker, rows)

# HTML speichern
with open('wetter.html', 'w', encoding='utf-8') as datei:
    datei.write(html_inhalt)

print("HTML-Datei mit Wetter wurde erstellt: wetter.html")

# HTML im Browser öffnen
webbrowser.open('wetter.html')
