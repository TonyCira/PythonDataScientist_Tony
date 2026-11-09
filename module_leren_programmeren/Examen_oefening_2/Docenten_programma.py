from tabulate import tabulate
import csv

# =====================
# DATA INLEZEN
# =====================

def lees_campus(campus):
    with open(campus + ".csv", "r", newline ="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        docenten = list(reader)
    return headers, docenten

# =====================
# DATA wegschrijven
# =====================
def schrijf_campus(campus,docenten):
    with open(campus + ".csv", "w", newline ="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(docenten)

# =======================
# HULPFUNCTIONALITEITEN
# =======================

def vraag_campus(tekst="Campus: "):
    campus = input(tekst).lower()
    if campus in campussen:
        return campus
    print("Onbekende campus")
    return None


# =====================
# FUNCTIONALITEITEN
# =====================

def toon_alle_docenten():
    for campus, docenten in campussen.items():
        print(f"\nCampus {campus.capitalize()}")
        print(tabulate(docenten, headers=headers))


def toon_alle_docenten_van_campus_naar_keuze():
    campus = vraag_campus()
    if campus:
        print(tabulate(campussen[campus], headers=headers))



def toon_alle_unieke_departementen_van_campus_naar_keuze():
    campus = vraag_campus()
    if campus:
        departementen = sorted(set([docent[5] for docent in campussen[campus]]))
        for nummer, deparment in enumerate(departementen):
            print(nummer, deparment)


def toon_docenten_ouder_dan():
    leeftijd= int(input("Ouder dan: "))
    for campus, docenten in campussen.items():
        res = [d for d in docenten if int(d[2]) > leeftijd]
        print(f"\nCampus {campus.capitalize()}: {len(res)} docenten")
        if res:
            print(tabulate(res, headers=headers))

def Toon_alle_docenten_met_loon_hoger_dan():
    loon= int(input("Loon hoger dan: "))
    for campus, docenten in campussen.items():
        res = [d for d in docenten if int(d[6]) > loon]
        print(f"\nCampus {campus.capitalize()}: {len(res)} docenten")
        if res:
            print(tabulate(res, headers=headers))

def voeg_een_docent_toe():
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
            [voornaam,achternaam, leeftijd, gemeente, geslacht, departement, loon]
        )
        print("docent toegevoegd")

def pas_het_loon_aan_van_docent():
    campus = vraag_campus()
    if campus:
        print(tabulate(campussen[campus], headers=headers, showindex = True))
        nummer = int(input("nummer van de docent: "))
        if 0 <= nummer < len(campussen[campus]):
            nieuw_loon = input("Nieuw loon: ")
            campussen[campus][nummer][6] = nieuw_loon
            print("Loon aangepast")
        else:
            print("Ongeldig nummer")

def verwijder_een_docent():
    campus = vraag_campus()
    if campus:
        print(tabulate(campussen[campus], headers=headers, showindex=True))
        nummer = int(input("Nummer van de docent: "))
        if 0 <= nummer < len(campussen[campus]):
            campussen[campus].pop(nummer)
            print("Docent verwijderd")
        else:
            print("Ongeldig nummer")

def verplaats_docent_van_campus():
    van = vraag_campus("Van Campus: ")
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


def toon_alle_docenten_per_campus():
    for campus, docenten in campussen.items():
        print(f"{campus.capitalize()}: {len(docenten)} docenten")


# =====================
# DATA wegschrijven
# =====================

def update_data():
    for campus, docenten in campussen.items():
        schrijf_campus(campus, docenten)
    print("Data weggeschreven naar de cvs's")


# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle_docenten,
    "2": toon_alle_docenten_van_campus_naar_keuze,
    "3": toon_alle_unieke_departementen_van_campus_naar_keuze,
    "4": toon_docenten_ouder_dan,
    "5": Toon_alle_docenten_met_loon_hoger_dan,
    "6": voeg_een_docent_toe,
    "7": pas_het_loon_aan_van_docent,
    "8": verwijder_een_docent,
    "9": verplaats_docent_van_campus,
    "10": toon_alle_docenten_per_campus,
    "11": update_data

}

# =====================
# HOOFDLUS
# =====================

campussen = {}
for campus in ["genk","pelt"]:
    headers, campussen[campus] = lees_campus(campus)


while True:

    print("\n")
    print("=" * 40)
    print("      Syntra Docenten")
    print("=" * 40)
    print("1  - Toon alle docenten")
    print("2  - Toon alle docenten van campus naar keuze")
    print("3  - Toon alle unieke departementen van campus naar keuze")
    print("4  - Toon docenten ouder dan")
    print("5  - Toon alle docenten met loon hoger dan")
    print("6  - voeg een docent toe")
    print("7  - pas het loon aan van docent")
    print("8  - verwijder een docent")
    print("9  - verplaats docent naar campus naar keuze")
    print("10 - toon alle docenten per campus")
    print("11 - update data")
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
