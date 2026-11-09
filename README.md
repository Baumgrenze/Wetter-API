Meine pip version hat erst Heute funktioniert. Nachdem alles was ich versucht habe nicht gegangen ist habe ich komplett python 3.14 installiert und jetzt geht es.
Wegen diesem Zeitstress habe ich anstatt Chess API die Wetter API gemacht. die KI hat die main.py leicht modifiziert mit den design. Zeilen. Der rest ist von hand.

Read me:


# 🌦️ Wetter-Check

Ein kleines Python-Programm für das Terminal: Du gibst eine Stadt ein und bekommst das aktuelle Wetter
mit Bild, Farben und einem Tipp. Die Daten kommen von der **OpenWeatherMap-API**.

## Beispiel

```text
╔════════════════════╗
║    WETTER-CHECK    ║
╚════════════════════╝
Für welche Stadt willst du das Wetter wissen? Wien

Wetter in Wien: leichter Regen

      .--.
   .-(    ).
  (___.__)__)
   / / / / /
  / / / / /

Temperatur: 8.4 °C ████████
Gefühlt: 6.1 °C
Luftfeuchtigkeit: 84 %
Wind: 11.2 km/h

Tipp: Regenschirm nicht vergessen!
```

*Die Werte sind Beispielwerte. Im Terminal ist alles farbig: Das Bild passt zum Wetter (bei klarer Nacht
gibt es einen Mond), der Temperatur-Balken wird je nach Temperatur blau, gelb oder rot.*

## So startest du es

1. Bibliothek installieren: `pip install requests`
2. Kostenlosen API-Key holen: auf [openweathermap.org](https://home.openweathermap.org/users/sign_up)
   registrieren und danach unter *API keys* den Key kopieren.
   Ein neuer Key kann bis zu ca. 2 Stunden brauchen, bis er funktioniert.
3. Den Key in `main.py` einfügen: `API_KEY = "DEIN_API_KEY"`
4. Starten: `python main.py`

**Wichtig:** Den Key nicht öffentlich auf GitHub hochladen. Vor dem Hochladen wieder durch `DEIN_API_KEY` ersetzen.

**Design ansehen, ohne Key:** `python design.py` zeigt alle Bilder.

Am besten im normalen Terminal oder in VS Code starten. Die IDLE-Shell kann keine Farben darstellen.

## Dateien

| Datei | Aufgabe |
|---|---|
| `main.py` | Schnittstelle abfragen, Werte aus der Antwort holen, ausgeben |
| `design.py` | Aussehen: Farben, ASCII-Bilder, Temperatur-Balken, Tipps, Fehlermeldungen |

## So funktioniert die Schnittstelle

Das Programm schickt eine Anfrage an diese Adresse:

```text
https://api.openweathermap.org/data/2.5/weather?q=STADT&appid=KEY&units=metric&lang=de
```

- `q` ist die Stadt, `appid` der API-Key, `units=metric` bedeutet Celsius, `lang=de` bedeutet deutsch.
- Die Antwort kommt als JSON. Mit `.json()` macht die Bibliothek `requests` daraus ein Dictionary.
- Der Statuscode sagt, ob es geklappt hat: 200 = ok, 404 = Stadt nicht gefunden, 401 = Key falsch oder noch nicht aktiv.

Diese Werte holt das Programm aus der Antwort:

| Wert | Bedeutung |
|---|---|
| `daten["name"]` | Name der Stadt |
| `daten["weather"][0]["description"]` | Beschreibung des Wetters |
| `daten["weather"][0]["main"]` | Wettertyp (Clear, Clouds, Rain, Snow, ...), bestimmt das Bild |
| `daten["weather"][0]["icon"]` | Icon-Code, er endet nachts auf `n`, dann gibt es den Mond statt der Sonne |
| `daten["main"]["temp"]` | Temperatur in °C |
| `daten["main"]["feels_like"]` | gefühlte Temperatur in °C |
| `daten["main"]["humidity"]` | Luftfeuchtigkeit in % |
| `daten["wind"]["speed"]` | Wind in m/s, mal 3,6 sind es km/h |

Hinweis: Die Suche mit dem Stadtnamen (`q=`) ist bei OpenWeatherMap als veraltet markiert, funktioniert aber noch.

## Quellen

- OpenWeather: [Current weather data](https://openweathermap.org/current)
