import csv
from tabulate import tabulate

bestand = "muzikanten.csv"


# =====================
# INLEZEN EN WEGSCHRIJVEN
# =====================

def lees_csv():
    with open(bestand, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list(reader)
    return headers, data


def update_data():
    with open(bestand, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    print("Data opgeslagen in", bestand)


# =====================
# TONEN
# =====================

def toon_alle():
    print(tabulate(data, headers=headers, showindex=True))


def toon_genres():
    genres = sorted(set([rij[3] for rij in data]))
    for nummer, genre in enumerate(genres):
        print(nummer, genre)


def toon_instrumenten():
    instrumenten = sorted(set([rij[4] for rij in data]))
    for nummer, instrument in enumerate(instrumenten):
        print(nummer, instrument)


def toon_per_instrument():
    instrument = input("Welk instrument? ").lower()
    res = [rij for rij in data if rij[4].lower() == instrument]
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten")


def toon_per_genre():
    genre = input("Welk genre? ").lower()
    res = [rij for rij in data if rij[3].lower() == genre]
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten")


def toon_per_geslacht():
    geslacht = input("Geslacht (M/V)? ").upper()
    res = [rij for rij in data if rij[2] == geslacht]
    print(tabulate(res, headers=headers))


def toon_onder_prijs():
    prijs = int(input("Maximaal uurtarief: "))
    res = [rij for rij in data if int(rij[5]) < prijs]
    res = sorted(res, key=lambda rij: int(rij[5]))
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten onder de {prijs} euro per uur")


def toon_boven_prijs():
    prijs = int(input("Minimaal uurtarief: "))
    res = [rij for rij in data if int(rij[5]) > prijs]
    res = sorted(res, key=lambda rij: int(rij[5]), reverse=True)
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten boven de {prijs} euro per uur")


def zoek_op_achternaam():
    zoek = input("Zoek op (een deel van) de achternaam: ").lower()
    res = [rij for rij in data if zoek in rij[1].lower()]
    print(tabulate(res, headers=headers))


def toon_sorteer_op_tarief():
    res = sorted(data, key=lambda rij: int(rij[5]), reverse=True)
    print(tabulate(res, headers=headers))


# =====================
# TELLEN, SETS EN TUPLE
# =====================

def toon_aantal_per_genre():
    aantal = {}
    for rij in data:
        genre = rij[3]
        aantal[genre] = aantal.get(genre, 0) + 1
    for genre, n in sorted(aantal.items()):
        print(f"{genre}: {n}")


def toon_genre_niet_instrument():
    genre = input("Welk genre spelen ze? ").lower()
    instrument = input("Welk instrument spelen ze niet? ").lower()
    in_genre = set([rij[0] + " " + rij[1] for rij in data if rij[3].lower() == genre])
    met_instrument = set([rij[0] + " " + rij[1] for rij in data if rij[4].lower() == instrument])
    for naam in sorted(in_genre - met_instrument):
        print(naam)


def bereken_min_max():
    tarieven = [int(rij[5]) for rij in data]
    return min(tarieven), max(tarieven)


def toon_statistiek():
    tarieven = [int(rij[5]) for rij in data]
    laagste, hoogste = bereken_min_max()
    gemiddelde = round(sum(tarieven) / len(tarieven), 2)
    print(f"Laagste tarief: {laagste}")
    print(f"Hoogste tarief: {hoogste}")
    print(f"Gemiddeld tarief: {gemiddelde}")


# =====================
# TOEVOEGEN, AANPASSEN, VERWIJDEREN
# =====================

def voeg_toe():
    voornaam = input("Voornaam: ").capitalize()
    achternaam = input("Achternaam: ").title()
    geslacht = input("Geslacht (M/V): ").upper()
    genre = input("Genre: ").capitalize()
    instrument = input("Instrument: ").capitalize()
    uurtarief = int(input("Uurtarief: "))
    data.append([voornaam, achternaam, geslacht, genre, instrument, uurtarief])
    print("Muzikant toegevoegd")


def verwijder():
    toon_alle()
    nummer = int(input("Nummer van de muzikant: "))
    if 0 <= nummer < len(data):
        data.pop(nummer)
        print("Muzikant verwijderd")
    else:
        print("Ongeldig nummer")


def pas_genre_of_instrument_aan():
    toon_alle()
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
        print("Ongeldig nummer")


def pas_tarief_aan():
    toon_alle()
    nummer = int(input("Nummer van de muzikant: "))
    if 0 <= nummer < len(data):
        data[nummer][5] = int(input("Nieuw uurtarief: "))
        print("Tarief aangepast")
    else:
        print("Ongeldig nummer")


# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle,
    "2": toon_genres,
    "3": toon_instrumenten,
    "4": toon_per_instrument,
    "5": toon_per_genre,
    "6": toon_per_geslacht,
    "7": toon_onder_prijs,
    "8": toon_boven_prijs,
    "9": zoek_op_achternaam,
    "10": toon_sorteer_op_tarief,
    "11": toon_aantal_per_genre,
    "12": toon_genre_niet_instrument,
    "13": toon_statistiek,
    "14": voeg_toe,
    "15": verwijder,
    "16": pas_genre_of_instrument_aan,
    "17": pas_tarief_aan,
    "18": update_data,
}


def toon_menu():
    print("\n" + "=" * 40)
    print("      MUZIKANTEN")
    print("=" * 40)
    print("1  - Toon alle muzikanten")
    print("2  - Toon alle unieke genres")
    print("3  - Toon alle unieke instrumenten")
    print("4  - Toon muzikanten met instrument x")
    print("5  - Toon muzikanten met genre x")
    print("6  - Toon jongens of meisjes")
    print("7  - Toon muzikanten onder vraagprijs x")
    print("8  - Toon muzikanten boven vraagprijs x")
    print("9  - Zoek op achternaam")
    print("10 - Sorteer op uurtarief (aflopend)")
    print("11 - Toon aantal muzikanten per genre")
    print("12 - Toon genre x maar niet instrument y")
    print("13 - Toon laagste, hoogste en gemiddeld tarief")
    print("14 - Voeg muzikant toe")
    print("15 - Verwijder muzikant")
    print("16 - Pas genre of instrument aan")
    print("17 - Pas uurtarief aan")
    print("18 - Update data (opslaan)")
    print("0  - Stoppen (slaat ook op)")


# =====================
# HOOFDPROGRAMMA
# =====================

headers, data = lees_csv()

while True:
    toon_menu()
    keuze = input("\nMaak een keuze: ")

    if keuze == "0":
        update_data()
        print("Programma afgesloten.")
        break

    if keuze in functies:
        functies[keuze]()
    else:
        print("Ongeldige keuze.")
