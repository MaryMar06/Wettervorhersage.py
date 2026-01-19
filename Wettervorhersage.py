import requests
from datetime import datetime
import webbrowser

api_schluessel = '972aafaa3761633381bef65cd97bfeb4'
staedte = ['Mannheim', 'Berlin', 'Sevastopol', 'Kiev']

# Читаем шаблон HTML
with open('index.html', 'r', encoding='utf-8') as datei:
    html_inhalt = datei.read()

insert_marker = '<!-- Python wird hier die Daten einfügen -->'
rows = ''

for stadt in staedte:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={stadt}&units=metric&lang=de&appid={api_schluessel}'
    antwort = requests.get(url)
    daten = antwort.json()
    zeit = datetime.now().strftime('%d.%m.%Y %H:%M')

    if 'main' in daten:
        temperatur = daten['main']['temp']
        gefuehlt = daten['main']['feels_like']
        beschreibung = daten['weather'][0]['description']

        # Вывод в PowerShell
        print(f'{stadt} ({zeit}): {temperatur}°C, gefühlt {gefuehlt}°C, {beschreibung}')

        # Добавляем строку в HTML
        rows += f"""
        <tr>
            <td>{stadt} ({zeit})</td>
            <td>{temperatur}°C</td>
            <td>{gefuehlt}°C</td>
            <td>{beschreibung}</td>
        </tr>
        """
    else:
        print(f"{stadt}: Fehler – Stadt nicht gefunden oder API-Key ungültig")
        rows += f"""
        <tr>
            <td>{stadt}</td>
            <td colspan="3">Fehler: Stadt nicht gefunden oder API-Key ungültig</td>
        </tr>
        """

# Вставляем строки в HTML
html_inhalt = html_inhalt.replace(insert_marker, rows)

# Сохраняем HTML
html_datei = 'wetter.html'
with open(html_datei, 'w', encoding='utf-8') as datei:
    datei.write(html_inhalt)

print(f"HTML-Datei mit Wetter wurde erstellt: {html_datei}")

# Автоматически открываем браузер
webbrowser.open(html_datei)
