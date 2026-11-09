import csv
from tabulate import tabulate

bestand = "studenten.csv"

def lees_csv(bestand):
    with open(bestand, "r", newline="") as f:
        data = csv.reader(f)
        headers = next(data)
        rijen = list(data)

    return headers, rijen


def schrijf_csv(bestand, headers, rijen):
    with open(bestand, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rijen)

def toon_studenten(headers, studenten):
    print(tabulate(studenten, headers=headers, showindex=True))

def return_namen(studenten):
    namen = []
    for student in studenten:
        namen.append(student[0])
    return namen

def return_klassen(studenten):
    klassen = []
    for student in studenten:
        klassen.append(student[1])
    return klassen

def return_woonplaats(studenten):
    woonplaatsen = []
    for student in studenten:
        woonplaatsen.append(student[2])
    return woonplaatsen

def toon_namen(studenten):
    namen = sorted(set([student[0] for student in studenten]))
    print("Namen van de studenten")
    print("-----------------------------")
    for nummer, naam in enumerate(namen):
        print(nummer, naam)

def toon_klassen(studenten):
    klassen = sorted(set([student[1] for student in studenten]))
    print("klassen van de studenten")
    print("-----------------------------")
    for nummer, klas in enumerate(klassen):
        print(nummer, klas)

def toon_woonplaatsen(studenten):
    woonplaatsen = sorted(set([student[2] for student in studenten]))
    print("Woonplaatsen van de studenten")
    print("-----------------------------")
    for nummer, woonplaats in enumerate(woonplaatsen):
        print(nummer, woonplaats)

def zoek_student(headers, studenten):
    naam = input("welke naam zoek je: ").capitalize()
    namen = return_namen(studenten)
    if naam in namen:
        plaatsnummer = namen.index(naam)
        print(f"{naam} komt voor op plaats {plaatsnummer}")
        print(tabulate([studenten[plaatsnummer]], headers=headers))
    else:
        print("naam niet gevonden")


def voeg_student_toe(studenten):
    naam = input("naam: ").capitalize()
    klas = input("klas: ").lower()
    woonplaats = input("woonplaats: ").capitalize()
    studenten.append([naam, klas, woonplaats])

def verander_woonplaats(headers, studenten):
    toon_studenten(headers, studenten)
    nummer = int(input("nummer van de student: "))
    if 0 <= nummer < len(studenten):
        studenten[nummer][2] = input("nieuwe woonplaats: ").capitalize()
    else:
        print("nummer niet gevonden")

def verwijder_student(headers, studenten):
    toon_studenten(headers, studenten)
    nummer = int(input("nummer van de student: "))
    if 0 <= nummer < len(studenten):
        studenten.pop(nummer)
    else:
        print("nummer niet gevonden")

def uniek_woonplaats(studenten):
    woonplaatsen = set()
    for student in studenten:
        woonplaatsen.add(student[2])
    return woonplaatsen



def toon_menu():
    print("1: toon alle studenten")
    print("2: zoek een student")
    print("3: voeg een student toe")
    print("4: verander de woonplaats")
    print("5: verwijder een student")
    print("6: toon de unieke woonplaatsen")
    print("7: toon de namen")
    print("8: toon de klassen")
    print("9: toon de woonplaatsen")
    print("stop: opslaan en stoppen")

##### hoofdprogramma ########

headers, studenten = lees_csv(bestand)

toon_menu()
keuze = input("maak je keuze: ").lower()
while keuze != "stop":
    if keuze == "1":
        toon_studenten(headers, studenten)
    elif keuze == "2":
        zoek_student(headers, studenten)
    elif keuze == "3":
        voeg_student_toe(studenten)
    elif keuze == "4":
        verander_woonplaats(headers, studenten)
    elif keuze == "5":
        verwijder_student(headers, studenten)
    elif keuze == "6":
        print(sorted(uniek_woonplaats(studenten)))
    elif keuze == "7":
        toon_namen(studenten)
    elif keuze == "8":
        toon_klassen(studenten)
    elif keuze == "9":
        toon_woonplaatsen(studenten)
    else:
        print("verkeerde invoer")

    toon_menu()
    keuze = input("maak je keuze: ").lower()

schrijf_csv(bestand, headers, studenten)
print("opgeslagen")

