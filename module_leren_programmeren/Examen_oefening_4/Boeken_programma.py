import csv
from tabulate import tabulate

bestand = "boeken.csv"

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

def toon_alle_boeken():
    print(tabulate(data, headers=headers, showindex=True))

def toon_per_genre():
    genre = input("Van welk genre wil je de boeken zien?: ").lower()
    res = [rij for rij in data if rij[2].lower() == genre]  # als ik hier capitalize had gebruikt bij ingave genre had ik hier niet met lower moeten werken ik zie dit nu om dat lijst niet groot is, maar bij veel data altijd beter om alles om te vormen om zekerheid te hebben bij data controle
    print(tabulate(res, headers=headers))

def toon_onder_prijs():
    prijs = float(input("Geef boeken goedkoper dan: "))
    res = [rij for rij in data if float(rij[4]) < prijs]
    res = sorted(res, key=lambda rij: float(rij[4]))
    print(tabulate(res, headers=headers))

def toon_aantal_boeken_per_genre():
    aantal = {}
    for rij in data:
        genre = rij[2]
        aantal[genre] = aantal.get(genre, 0) + 1
    for genre, n in sorted(aantal.items()):
        print(f"{genre}: {n} boeken")

# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle_boeken,
    "2": toon_per_genre,
    "3": toon_onder_prijs,
    "4": toon_aantal_boeken_per_genre,
    "5": update_data,
}


def toon_menu():
    print("\n" + "=" * 40)
    print("      BOEKEN")
    print("=" * 40)
    print("1  - Toon alle boeken")
    print("2  - Toon alle per genre")
    print("3  - Toon alle boeken onder prijs")
    print("4  - Toon aantal boeken per genre")
    print("5  - update data")
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
