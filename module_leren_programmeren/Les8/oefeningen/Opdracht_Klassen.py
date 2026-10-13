klassen = {
    "1A": ["Tom", "An", "Piet"],
    "1B": ["Sara", "Jan"],
    "1C": []                       # lege klas = lege lijst, geen lege string
}

def toon_klassen():
    for klas, leerlingen in klassen.items():
        print(f"klas {klas}: {len(leerlingen)} leerlingen")
        for leerling in leerlingen:
            print("    -", leerling)



def voeg_leerling_toe():
    toon_klassen()
    klas = input("in welke klas wil je een leerling toevoegen").upper()
    if klas in klassen:
        naam = input("Naam leerling: ").capitalize()
        klassen[klas].append(naam)
        print(f"{naam} toegevoegd aan {klas}")

    else:
        print("klas bestaat niet")


def pas_naam_leerling_aan():
    toon_klassen()
    klas = input("in welke klas wil je een leerling aanpassen")
    if klas in klassen:
        naam = input("Naam leerling: ").capitalize()
        klassen[leerling].append(naam)
        print(f"{naam} aangepast in {klas}")
    else:
        print("klas of leerling bestaan niet")



