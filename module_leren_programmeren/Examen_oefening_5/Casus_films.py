import csv
from tabulate import tabulate

bestand = "films.csv"

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

def toon_alle_films():
    print(tabulate(data, headers=headers, showindex=True))


def toon_films_van_genre():
    genre = input("Voor welke genre wil je films zien? ").lower()
    res = [rij for rij in data if genre.lower() in rij[2].lower().split(";")]
    res = sorted(res, key=lambda rij: float(rij[4]))
    print(tabulate(res, headers=headers))

def toon_unieke_genres():
    genres = set()
    for rij in data:
        lijst = rij[2].split(";")
        for genre in lijst:
            if genre != "":
                genres.add(genre)
    for nummer, genre in enumerate(sorted(genres)):
        print(nummer, genre)

# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle_films,
    "2": toon_films_van_genre,
    "3": toon_unieke_genres,
    "4": update_data,
}


def toon_menu():
    print("\n" + "=" * 40)
    print("      FILMS")
    print("=" * 40)
    print("1  - Toon alle films")
    print("2  - Toon films van genre")
    print("3  - Toon genres")
    print("4  - update data")
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
