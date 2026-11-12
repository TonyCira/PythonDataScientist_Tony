import csv
from tabulate import tabulate

bestand = "dataset_diersoorten.csv"

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
# FUNCTIONALITEITEN
# =====================

def toon_alle_data():
    print(tabulate(data, headers=headers, showindex=True))

def toon_alle_unieke_diersoorten():
    diersoorten = sorted(set([rij[1] for rij in data]))
    for nummer, diersoort in enumerate(diersoorten):
            print(nummer, diersoort)

def toon_alle_unieke_landen():
    landen = sorted(set([rij[4] for rij in data]))
    for nummer, land in enumerate(landen):
        print(nummer, land)

def toon_dieren_van_diersoort():
    diersoort = input("Van welke diersoort wil je de dieren zien? ").lower()
    res = [rij for rij in data if rij[1].lower() == diersoort]
    print(tabulate(res, headers=headers))

def voeg_dier_toe():
    naam_dier = input("Geef naam van dier: ").title()
    dier_soort = input("Geef soort van dier: ").capitalize()
    latijnse_naam = input("Geef naam van latijnse naam: ").capitalize()
    m_v = input("Geef geslacht van dier: ").Upper()
    land_van_oorkomst = input("Geef land van oorkomst van dier: ").capitalize()
    lengte_in_cm = int(input("Geef lengte van dier in cm: "))
    gewicht_in_kilo = float(input("Geef gewicht van dier in kilo's: "))
    data.append([naam_dier, dier_soort, latijnse_naam, m_v, land_van_oorkomst, lengte_in_cm, gewicht_in_kilo])
    print("Dier toegevoegd")


def verwijder_dier():
    toon_alle_data()
    nummer = int(input("Geef nummer van het dier voor te verwijderen: "))
    if 0 <= nummer < len(data):
        data.pop(nummer)
        print("Dier verwijderd")
    else:
        print("Ongeldig nummer")


def pas_gewicht_aan_van_dier():
    toon_alle_data()
    nummer = int(input("Geef nummer van het dier om gewicht aan te passen: "))
    if 0 <= nummer < len(data):
        data[nummer][6] = float(input("Nieuw gewicht: "))
        print("Gewicht aangepast")
    else:
        print("Ongeldig nummer")


def toon_dieren_boven_kilo():
    gewicht = float(input("Minimum gewicht: "))
    res = [rij for rij in data if int(rij[6]) > gewicht]
    res = sorted(res, key=lambda rij: int(rij[6]))
    print(tabulate(res, headers=headers))

def toon_dier_sorteer_op_naam():
    res = sorted(data, key=lambda rij: int(rij[0]))
    print(tabulate(res, headers=headers))



# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle_data,
    "2": toon_alle_unieke_diersoorten,
    "3": toon_alle_unieke_landen,
    "4": toon_dieren_van_diersoort,
    "5": voeg_dier_toe,
    "6": verwijder_dier,
    "7": pas_gewicht_aan_van_dier,
    "8": toon_dieren_boven_kilo,
    "9": toon_dier_sorteer_op_naam,
    "10": update_data,
}


def toon_menu():
    print("\n" + "=" * 40)
    print("      DIERSOORTEN")
    print("=" * 40)
    print("1  - Toon alle dieren")
    print("2  - Toon alle unieke diersoorten")
    print("3  - Toon alle unieke landen")
    print("4  - Toon alle dier van diersoort")
    print("5  - Voeg een dier toe")
    print("6  - Verwijder een dier")
    print("7  - Pas het gewicht aan van een dier")
    print("8  - Toon alle dieren zwaarder dan x kilo")
    print("9  - Sorteer op naam van dieren")
    print("10 - update data")
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
