import csv
from tabulate import tabulate

bestand = "cursisten.csv"

# =====================
# DATA INLEZEN
# =====================

def lees_csv(bestand):
    with open(bestand, "r", newline ="", encoding="utf-8") as f:
        data = csv.reader(f)
        headers = next(data)
        cursisten = list(data)

    return headers, cursisten

headers, cursisten = lees_csv(bestand)

# =====================
# DATA WEGSCHRIJVEN
# =====================

def update_data():
    with open(bestand, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(cursisten)

    print("Data opgeslagen in cursisten.csv")

# =====================
# FUNCTIONALITEITEN
# =====================


def toon_cursisten():
    print(tabulate(cursisten, headers=headers, showindex=True))


def toon_cursisten_van_cursus():
    cursus = input("Voor welke cursus zoek je cursisten? ").lower()
    res = [c for c in cursisten if cursus in c[2].lower().split(";")]
    res = sorted(res, key=lambda c: float(c[3]), reverse=True)
    print(tabulate(res, headers=headers))

def zoek_cursusA_Y_cursusB_N():
    cursus_a = input("Geef de cursus die de cursist volgt: ").lower()
    cursus_b = input("Geef de cursus die de cursist niet volgt: ").lower()
    volgt_a = set([c[0] for c in cursisten if cursus_a in c[2].lower().split(";")])
    volgt_b = set([c[0] for c in cursisten if cursus_b in c[2].lower().split(";")])
    for naam in sorted(volgt_a - volgt_b):
        print(naam)


def voeg_cursist_toe():
    naam = input("Geef voornaam + naam van de cursist: ").title()
    woonplaats = input("Geef de woonplaats van de cursist: ").capitalize()
    cursussen = input("Geef de cursussen(gescheiden door een komma): ")
    cursussen = ";".join([x.strip() for x in cursussen.split(",")])
    score = float(input("geef een score: "))
    cursisten.append([naam, woonplaats, cursussen, score])



# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_cursisten,
    "2": toon_cursisten_van_cursus,
    "3": zoek_cursusA_Y_cursusB_N,
    "4": voeg_cursist_toe,
    "5": update_data

}


# =====================
# HOOFDLUS
# =====================

while True:

    print("\n")
    print("=" * 40)
    print("      CURSISTEN")
    print("=" * 40)
    print("1  - Toon alle cursisten")
    print("2  - Toon cursisten van cursus")
    print("3  - zoek cursist voor cursus maar niet voor cursus")
    print("4  - voeg cursist toe")
    print("5  - update data")
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