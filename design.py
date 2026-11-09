# design.py - hier steckt alles, was schön aussehen soll: Farben, Bilder und Tipps
import os

os.system("")  # kleiner Trick, damit Farben auch in der Windows-Konsole funktionieren

# Farben fürs Terminal: Alles nach einem Farbcode wird bunt, NORMAL schaltet die Farbe wieder aus
NORMAL = "\033[0m"
GRAU = "\033[2m"
BLAU = "\033[94m"
CYAN = "\033[36m"
GELB = "\033[33m"
ROT = "\033[91m"

# Bilder aus Zeichen (ASCII-Art)
SONNE = """
    *   |   *
     .-----.
 ---(       )---
     '-----'
    *   |   *
"""

MOND = """
   ▄▄██▀    *
  ▄███     .
  ████   *
  ▀███▄     .
   ▀▀███▀   *
"""

WOLKE = """
      .--.
   .-(    ).
  (___.__)__)
        .-.
       (___)
"""

REGEN = """
      .--.
   .-(    ).
  (___.__)__)
   / / / / /
  / / / / /
"""

SCHNEE = """
      .--.
   .-(    ).
  (___.__)__)
   *  *  *  *
  *  *  *  *
"""

GEWITTER = """
      .--.
   .-(    ).
  (___.__)__)
    /  /  /
   /_ /_ /_
"""

NEBEL = """
 _ - _ - _ - _
  _ - _ - _ - _
 _ - _ - _ - _
  _ - _ - _ - _
"""


def zeige_titel():
    print(CYAN + "╔════════════════════╗")
    print("║    WETTER-CHECK    ║")
    print("╚════════════════════╝" + NORMAL)


def zeige_bild(wetter, nacht):
    # das Bild passend zum Wetter auswählen und in der passenden Farbe zeigen
    if wetter == "Clear" and nacht:
        print(MOND)
    elif wetter == "Clear":
        print(GELB + SONNE + NORMAL)
    elif wetter == "Clouds":
        print(GRAU + WOLKE + NORMAL)
    elif wetter == "Rain" or wetter == "Drizzle":
        print(BLAU + REGEN + NORMAL)
    elif wetter == "Snow":
        print(CYAN + SCHNEE + NORMAL)
    elif wetter == "Thunderstorm":
        print(GELB + GEWITTER + NORMAL)
    else:  # Nebel, Dunst, Rauch, ...
        print(GRAU + NEBEL + NORMAL)


def zeige_temperatur(temperatur):
    # je kälter, desto blauer - je wärmer, desto roter
    if temperatur < 0:
        farbe = BLAU
    elif temperatur < 10:
        farbe = CYAN
    elif temperatur < 20:
        farbe = NORMAL
    elif temperatur < 28:
        farbe = GELB
    else:
        farbe = ROT
    balken = "█" * round(temperatur)  # ein Block pro Grad
    print("Temperatur:", round(temperatur, 1), "°C", farbe + balken + NORMAL)


def zeige_tipp(wetter, nacht):
    if wetter == "Clear" and nacht:
        tipp = "Klare Nacht - perfekt zum Sterne schauen."
    elif wetter == "Clear":
        tipp = "Sonnenbrille einpacken und raus an die frische Luft!"
    elif wetter == "Clouds":
        tipp = "Bewölkt, aber trocken - ein Spaziergang geht immer."
    elif wetter == "Rain" or wetter == "Drizzle":
        tipp = "Regenschirm nicht vergessen!"
    elif wetter == "Snow":
        tipp = "Warm anziehen - vielleicht wird es ein Schneemann?"
    elif wetter == "Thunderstorm":
        tipp = "Gewitter! Lieber drinnen bleiben."
    else:
        tipp = "Schlechte Sicht - lieber vorsichtig sein."
    print()
    print("Tipp:", tipp)


def zeige_fehler(text):
    print(ROT + "Fehler: " + text + NORMAL)


# Vorschau ohne API-Key: "python design.py" zeigt alle Bilder.
# (Dieser Teil läuft nur, wenn man design.py direkt startet, nicht bei "import design".)
if __name__ == "__main__":
    zeige_titel()
    for wetter in ["Clear", "Clouds", "Rain", "Snow", "Thunderstorm", "Mist"]:
        print("-----", wetter)
        zeige_bild(wetter, False)
        zeige_tipp(wetter, False)
    print("----- Clear (Nacht)")
    zeige_bild("Clear", True)
    for temperatur in [-5, 5, 15, 25, 35]:
        zeige_temperatur(temperatur)
