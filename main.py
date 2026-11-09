import requests
import design  

#API-Key auf https://openweathermap.org holen und reinkopieren
API_KEY = "3a1f71f8a23302044725f6dfba417029"

design.zeige_titel()
stadt = input("Sag eine Stadt und ich gebe das Wetter aus ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={stadt}&appid={API_KEY}&units=metric&lang=de"

try:
    antwort = requests.get(url)

    if antwort.status_code == 200:
        daten = antwort.json()

        name = daten["name"]
        beschreibung = daten["weather"][0]["description"]
        wetter = daten["weather"][0]["main"]
        nacht = daten["weather"][0]["icon"].endswith("n")
        temperatur = daten["main"]["temp"]
        gefuehlt = daten["main"]["feels_like"]
        luftfeuchte = daten["main"]["humidity"]
        wind = daten["wind"]["speed"] * 3.6

        print()
        print("Wetter in", name + ":", beschreibung)
        design.zeige_bild(wetter, nacht)
        design.zeige_temperatur(temperatur)
        print("Gefühlt:", round(gefuehlt, 1), "°C")
        print("Luftfeuchtigkeit:", luftfeuchte, "%")
        print("Wind:", round(wind, 1), "km/h")
        design.zeige_tipp(wetter, nacht)

    elif antwort.status_code == 404:
        design.zeige_fehler("Diese Stadt gibts ned.")
    elif antwort.status_code == 401:
        design.zeige_fehler("Key vielleicht noch nicht aktiv, kann bissi dauern (oder einfach falsch).")
    else:
        design.zeige_fehler("Schnittstellenfehler: " + str(antwort.status_code))

except:
    design.zeige_fehler("Internet connection geht iwi ned")
