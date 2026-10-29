from tabulate import tabulate
import csv

# =====================
# DATA INLEZEN
# =====================

with open("klas.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    leerlingen = []
    for row in reader:
        leerlingen.append(row)

headers = leerlingen[0]
data = leerlingen[1:]

# =====================
# FUNCTIONALITEITEN
# =====================

def toon_alle_leerlingen():
    print(tabulate(data, headers=headers, showindex=True))


def toon_meisjes():
    meisjes = [x for x in data if x[3] == "V"]
    print(tabulate(meisjes, headers=headers))
    print(f"Er zijn {len(meisjes)} meisjes in de klas")

def toon_jongens():
    jongens = [x for x in data if x[3] == "M"]
    print(tabulate(jongens, headers=headers))
    print(f"Er zijn {len(jongens)} jongens in de klas")

def toon_iedereen_van_woonplaats():
    # result voorzien
    res = []
    woonplaats = input("In welke woonplaats zoek je studenten? ").capitalize()
    # indien de student woont in de gezochte gemeente dan toegevoegd aan de lijst
    for leerling in data:
        if woonplaats == leerling[4]:
            res.append(leerling)
    print(tabulate(res, headers=headers))

def voeg_leerling_toe():
    klas = input("Geef de klas: ").lower()
    leerling_id = input("Geef het id: ")
    naam = input("Geef naam van de leerling: ").title()
    geslacht = input("Geef het geslacht van de leerling: ").upper()
    woonplaats = input("Geef de woonplaats: ").capitalize()

    leerling = [klas, leerling_id, naam, geslacht, woonplaats]
    data.append(leerling)

def verwijder_leerling():
    # welke student
    toon_alle_leerlingen()
    leerling_nummer = int(input("Geef de nummer van de leerling: "))

    # is het ingegeven nummer kleiner dan het aantal studenten in de lijst
    if 0 <= leerling_nummer < len(data):
        #verwijder de leerling op basis van de index
        data.pop(leerling_nummer)
    else:
        print("leerling niet gevonden")

def sorteer_leerlingen_op_naam():

    res = sorted(data, key=lambda x: x[2])
    print(tabulate(res, headers=headers))


def update_data():
    with open("klas.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

    print("Data opgeslagen in klas.csv")

# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle_leerlingen,
    "2": toon_meisjes,
    "3": toon_jongens,
    "4": toon_iedereen_van_woonplaats,
    "5": voeg_leerling_toe,
    "6": verwijder_leerling,
    "7": sorteer_leerlingen_op_naam,
    "8": update_data

}

# =====================
# HOOFDLUS
# =====================

while True:

    print("\n")
    print("=" * 40)
    print("      Klasmanagement")
    print("=" * 40)
    print("1  - Toon alle leerlingen")
    print("2  - Toon meisjes")
    print("3  - Toon jongens")
    print("4  - Toon iedereen van woonplaats")
    print("5  - voeg leerling toe")
    print("6  - verwijder leerling")
    print("7  - sorteer op naam")
    print("8  - bewaar wijzigingen")
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