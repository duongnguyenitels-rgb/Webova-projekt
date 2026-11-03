# Skript prevede puvodni JPG fotky do WEBP ve 3 velikostech
# a vytvori jeden modro-bily placeholder obrazek.
# Spousti se z korenove slozky projektu prikazem:
#   python tools/obrazky.py
# Potrebuje knihovnu Pillow (pip install pillow).

import os
from PIL import Image, ImageDraw, ImageFont

# Slozka s puvodnimi fotkami (lezi mimo projekt, aby v nem nebyly JPG)
ZDROJ = "../originaly-jpg"
# Slozka, kam se ulozi hotove obrazky
CIL = "img"

# Puvodni nazev souboru -> novy nazev (bez pripony)
FOTKY = {
    "RazerMouse.jpg": "mys-v3",
    "RazerMouse2.jpg": "mys-v2",
    "Keyboard1.jpg": "klavesnice-1",
    "Keyboard2.jpg": "klavesnice-2",
}

# Sirky obrazku v pixelech, vyska se dopocita v pomeru 3:2
SIRKY = [400, 800, 1200]

MODRA = (21, 67, 140)
SVETLE_MODRA = (220, 233, 250)
BILA = (255, 255, 255)


def orizni_na_3_2(obrazek):
    # Vyrizne ze stredu fotky obdelnik v pomeru stran 3:2
    sirka, vyska = obrazek.size
    if sirka / vyska > 3 / 2:
        nova_sirka = int(vyska * 3 / 2)
        levy = (sirka - nova_sirka) // 2
        return obrazek.crop((levy, 0, levy + nova_sirka, vyska))
    else:
        nova_vyska = int(sirka * 2 / 3)
        horni = (vyska - nova_vyska) // 2
        return obrazek.crop((0, horni, sirka, horni + nova_vyska))


def uloz_velikosti(obrazek, nazev):
    # Ulozi obrazek ve vsech sirkach, napr. mys-v3-400.webp
    for sirka in SIRKY:
        vyska = sirka * 2 // 3
        mensi = obrazek.resize((sirka, vyska))
        soubor = os.path.join(CIL, nazev + "-" + str(sirka) + ".webp")
        mensi.save(soubor, "WEBP", quality=80)
        print("Ulozeno:", soubor)


def vytvor_placeholder():
    # Modre pozadi, bily obdelnik uprostred a text
    obrazek = Image.new("RGB", (1200, 800), MODRA)
    kresleni = ImageDraw.Draw(obrazek)
    kresleni.rectangle((150, 150, 1050, 650), fill=SVETLE_MODRA)
    kresleni.rectangle((300, 300, 900, 500), fill=BILA)
    # Arial umi ceske znaky; kdyz neni nainstalovany, pouzije se zakladni pismo
    try:
        pismo = ImageFont.truetype("arial.ttf", 60)
    except OSError:
        pismo = ImageFont.load_default(size=60)
    kresleni.text((600, 400), "Obsah balení", fill=MODRA, font=pismo, anchor="mm")
    uloz_velikosti(obrazek, "baleni")


os.makedirs(CIL, exist_ok=True)

for puvodni, novy in FOTKY.items():
    fotka = Image.open(os.path.join(ZDROJ, puvodni)).convert("RGB")
    uloz_velikosti(orizni_na_3_2(fotka), novy)

vytvor_placeholder()
