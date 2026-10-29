from tabulate import tabulate
import csv

# =====================
# DATA INLEZEN
# =====================

with open("muzikanten_data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    muzikanten = []
    for row in reader:
        muzikanten.append(row)

headers = muzikanten[0]
data = muzikanten[1:]

# =====================
# FUNCTIONALITEITEN
# =====================

def toon_alle_muzikanten():
    print(tabulate(data, headers=headers, showindex=True))

def toon_alle_genres():
    genres = sorted(set([x[3] for x in data]))

    for e, genre in enumerate(genres):
        print(e, genre, end="\t")
    print()

def toon_alle_instrumenten():
    instrumenten = sorted(set([x[4] for x in data]))

    for e, instrument in enumerate(instrumenten):
        print(e, instrument, end="\t")
    print()

def toon_iedereen_met_instrument():
    # result voorzien
    res = []
    instrument = input("Voor welke instrument zoek je muzikanten? ").capitalize()

    for muzikant in data:
        if instrument == data[4]:
            res.append(muzikant)
    print(tabulate(res, headers=headers))

def toon_iedereen_met_genre():
    # result voorzien
    res = []
    genre = input("Voor welke genre zoek je muzikanten? ").capitalize()

    for muzikant in data:
        if genre == data[3]:
            res.append(muzikant)
    print(tabulate(res, headers=headers))

def toon_iedereen_onder_vraagprijs():
    vraagprijs = int(input("Maximaal uurtarief: "))
    res = [x for x in data if int(x[5]) < vraagprijs]
    res = sorted(res, key=lambda x: int(x[5]))
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten onder de {vraagprijs} euro per uur")

def voeg_muzikant_toe():
    voornaam = input("Geef de voornaam van de muzikant: ").lower()
    achternaam = input("Geef de achternaam van de muzikant: ")
    geslacht = input("Geef het geslacht van de muzikant: ").title()
    genre = input("Geef het genre van de muzikant: ").upper()
    instrument = input("Geef het instrument: ").capitalize()
    uurtarief = input("Geef het uurtarief: ")

    leerling = [voornaam, achternaam, geslacht, genre, instrument, uurtarief]
    data.append(leerling)

def verwijder_muzikant():
    toon_alle_muzikanten()
    muzikant_nummer = int(input("Geef de nummer van de muzikant: "))

    if 0 <= muzikant_nummer < len(data):
        #verwijder de muzikant op basis van de index
        data.pop(muzikant_nummer)
    else:
        print("muzikant niet gevonden")

def pas_genre_of_instrument_aan():
    toon_alle_muzikanten()
    nummer = int(input("Nummer van de muzikant: "))

    if 0 <= nummer < len(data):
        keuze = input("Wil je het instrument of het genre aanpassen? ").lower()
        if keuze == "instrument":
            data[nummer][4] = input("Nieuw instrument: ").capitalize()
        elif keuze == "genre":
            data[nummer][3] = input("Nieuw genre: ").capitalize()
        else:
            print("Kies instrument of genre")
    else:
        print("ongeldig nummer")

def pas_het_uurtarief_aan():
    toon_alle_muzikanten()

    try:
        index = int(input("\nGeef het nummer van de muzikant: "))

        if 0 <= index < len(data):
            nieuw_uurtarief = int(input("Geef het nieuwe uurtarief: "))
            data[index][5] = nieuw_uurtarief
            print("uurtarief aangepast.")
        else:
            print("Kan uurtarief niet aanpassen.")

    except ValueError:
        print("Geef geldige gegevens in.")

def sorteer_op_uurtarief_aflopend():

    def uurtarief_key(x):
        return int(x[5])

    res = sorted(data, key=uurtarief_key, reverse=True)

    print(tabulate(res, headers=headers))

def update_data():
    with open("muzikanten_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

    print("Data opgeslagen in muzikanten_data.csv")

# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle_muzikanten,
    "2": toon_alle_genres,
    "3": toon_alle_instrumenten,
    "4": toon_iedereen_met_instrument,
    "5": toon_iedereen_met_genre,
    "6": toon_iedereen_onder_vraagprijs,
    "7": voeg_muzikant_toe,
    "8": verwijder_muzikant,
    "9": pas_genre_of_instrument_aan,
    "10": pas_het_uurtarief_aan,
    "11": sorteer_op_uurtarief_aflopend,
    "0": update_data

}

# =====================
# HOOFDLUS
# =====================

while True:

    print("\n")
    print("=" * 40)
    print("      Muzikanten")
    print("=" * 40)
    print("1  - Toon alle muzikanten")
    print("2  - Toon alle unieke genres")
    print("3  - Toon alle unieke instrumenten")
    print("4  - Toon iedereen met instrument")
    print("5  - Toon iedereen met genre")
    print("6  - Toon iedereen onder de vraagrpijs")
    print("7  - voeg muzikant toe")
    print("8  - verwijder een muzikant")
    print("9  - pas genre of instrument aan")
    print("10 - pas uurtarief aan")
    print("11 - sorteer op uurtarief aflopend")
    print("0  - stoppen")

    keuze = input("\nMaak een keuze: ")

    if keuze == "0":
        update_data()
        print("Programma afgesloten.")
        break

    if keuze in functies:
        functies[keuze]()
    else:
        print("Ongeldige keuze.")