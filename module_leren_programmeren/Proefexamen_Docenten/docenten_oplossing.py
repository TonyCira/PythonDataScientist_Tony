import csv
from tabulate import tabulate


def lees_campus(campus):
    with open(campus + ".csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        docenten = list(reader)
    return headers, docenten


def schrijf_campus(campus, docenten):
    with open(campus + ".csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(docenten)


def vraag_campus(tekst="Campus: "):
    campus = input(tekst).lower()
    if campus in campussen:
        return campus
    print("Onbekende campus")
    return None


# 1
def toon_alle_docenten():
    for campus, docenten in campussen.items():
        print(f"\nCampus {campus.capitalize()}")
        print(tabulate(docenten, headers=headers))


# 2
def toon_docenten_van_campus():
    campus = vraag_campus()
    if campus:
        print(tabulate(campussen[campus], headers=headers))


# 3
def toon_departementen():
    campus = vraag_campus()
    if campus:
        departementen = sorted(set([docent[5] for docent in campussen[campus]]))
        for nummer, departement in enumerate(departementen):
            print(nummer, departement)


# 4
def toon_ouder_dan():
    leeftijd = int(input("Ouder dan: "))
    for campus, docenten in campussen.items():
        res = [d for d in docenten if int(d[2]) > leeftijd]
        print(f"\nCampus {campus.capitalize()}: {len(res)} docenten")
        if res:
            print(tabulate(res, headers=headers))


# 5
def toon_loon_hoger():
    loon = int(input("Loon hoger dan: "))
    for campus, docenten in campussen.items():
        res = [d for d in docenten if int(d[6]) > loon]
        print(f"\nCampus {campus.capitalize()}: {len(res)} docenten")
        if res:
            print(tabulate(res, headers=headers))


# 6
def voeg_docent_toe():
    campus = vraag_campus()
    if campus:
        voornaam = input("Voornaam: ").capitalize()
        achternaam = input("Achternaam: ").capitalize()
        leeftijd = input("Leeftijd: ")
        gemeente = input("Gemeente: ").capitalize()
        geslacht = input("Geslacht (M/V): ").upper()
        departement = input("Departement: ")
        loon = input("Loon: ")
        campussen[campus].append(
            [voornaam, achternaam, leeftijd, gemeente, geslacht, departement, loon]
        )
        print("Docent toegevoegd")


# 7
def pas_loon_aan():
    campus = vraag_campus()
    if campus:
        print(tabulate(campussen[campus], headers=headers, showindex=True))
        nummer = int(input("Nummer van de docent: "))
        if 0 <= nummer < len(campussen[campus]):
            nieuw_loon = input("Nieuw loon: ")
            campussen[campus][nummer][6] = nieuw_loon
            print("Loon aangepast")
        else:
            print("Ongeldig nummer")


# 8
def verwijder_docent():
    campus = vraag_campus()
    if campus:
        print(tabulate(campussen[campus], headers=headers, showindex=True))
        nummer = int(input("Nummer van de docent: "))
        if 0 <= nummer < len(campussen[campus]):
            campussen[campus].pop(nummer)
            print("Docent verwijderd")
        else:
            print("Ongeldig nummer")


# 9
def verplaats_docent():
    van = vraag_campus("Van campus: ")
    if van:
        print(tabulate(campussen[van], headers=headers, showindex=True))
        nummer = int(input("Nummer van de docent: "))
        if 0 <= nummer < len(campussen[van]):
            naar = vraag_campus("Naar campus: ")
            if naar and naar != van:
                docent = campussen[van].pop(nummer)
                campussen[naar].append(docent)
                print(f"{docent[0]} {docent[1]} verplaatst van {van} naar {naar}")
            elif naar == van:
                print("Dat is dezelfde campus")
        else:
            print("Ongeldig nummer")


# 10
def toon_aantal_per_campus():
    for campus, docenten in campussen.items():
        print(f"{campus.capitalize()}: {len(docenten)} docenten")


# 11
def update_data():
    for campus, docenten in campussen.items():
        schrijf_campus(campus, docenten)
    print("Data weggeschreven naar de csv's")


def toon_menu():
    print("\n1. Toon alle docenten")
    print("2. Toon alle docenten van campus x")
    print("3. Toon alle unieke departementen van campus x")
    print("4. Toon docenten ouder dan x")
    print("5. Toon docenten met loon hoger dan x")
    print("6. Voeg een docent toe")
    print("7. Pas het loon aan van een docent")
    print("8. Verwijder een docent")
    print("9. Verplaats een docent van campus")
    print("10. Toon aantal docenten per campus")
    print("11. Update data (wegschrijven naar csv)")
    print("0. Stop")


menu = {
    "1": toon_alle_docenten,
    "2": toon_docenten_van_campus,
    "3": toon_departementen,
    "4": toon_ouder_dan,
    "5": toon_loon_hoger,
    "6": voeg_docent_toe,
    "7": pas_loon_aan,
    "8": verwijder_docent,
    "9": verplaats_docent,
    "10": toon_aantal_per_campus,
    "11": update_data,
}

# hoofdprogramma
campussen = {}
for campus in ["genk", "pelt"]:
    headers, campussen[campus] = lees_campus(campus)

while True:
    toon_menu()
    keuze = input("Keuze: ")
    if keuze == "0":
        break
    if keuze in menu:
        menu[keuze]()
    else:
        print("Ongeldige keuze")
