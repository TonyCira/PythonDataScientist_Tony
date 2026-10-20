from tabulate import tabulate
import csv

headers = ["naam", "klas", "woonplaats"]
studenten = [
    ["Anke", "1a", "As"],
    ["Ben", "1a", "Genk"],
    ["Fien", "2a", "Genk"],
    ["Cindy", "2b", "Hasselt"],
    ["Billy", "2b", "Hasselt"],
    ["Xindy", "1c", "Hasselt"]
 ]

def schrijf_data_weg():
    with open('studenten.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        studenten.insert(0, headers)
        data = studenten
        writer.writerow(data)


def schrijf_data_weg_2():
    with open('studenten2.csv', 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(studenten)

schrijf_data_weg_2()
schrijf_data_weg()


def toon_alle_studenten():
    data = tabulate(studenten, headers=headers, showindex=True)
    print(data)

def toon_alle_namen():
    for e , naam in enumerate(studenten):
        print(e, naam[0])


def return_namen():
    res = []
    for naam in studenten:
        res.append(naam[0])
    return res

print(*return_namen())

def voeg_student_toe():
    naam = input("Geef de naam: ")
    klas = input("geef de klas: ")
    woonplaats = input("geef de woonplaats: ")

    student = [naam, klas, woonplaats]
    studenten.append(student)

def verwijder_student():
    # welke student

    toon_alle_studenten()
    student_nummer = int(input("Geef de nummer van de student: "))

    # is het ingegeven nummer kleiner dan het aantal studenten in de lijst

    if student_nummer < len(studenten):
        #verwijder de leerling op basis van de index
        studenten.pop(student_nummer)
    else:
        print("student niet gevonden")


def bestaat_student():
    # wie
    naam = input("welke naam wil je opzoeken: ").capitalize()

    # naam controleren
    if naam in return_namen():
        namen = return_namen()
        plaatsnummer = namen.index(naam) # ook mogelijk op 1 regel : "plaatsnummer = return.namen().index(naam)"
        # feedback = bestaat en welke plaats
        print(f"{naam} komt voor in de lijst op plaats {plaatsnummer}")

    else:
        print("naam niet gevonden")


def toon_iedereen_van_woonplaats():
    # result voorzien
    res = []
    woonplaats = input("geef de woonplaats: ").capitalize()
    # indien de student woont in de gezochte gemeente dan toegevoegd aan de lijst
    for student in studenten:
        if woonplaats == student[2]:
            res.append(student)
    print(tabulate(res, headers=headers))

def verander_klas_van_student():
    # welke student
    toon_alle_namen()
    student_nummer = int(input("Geef de nummer van de student: "))
    if student_nummer < len(studenten):
        # nieuwe klas klas toevoegen vragen welke nieuwe en koppelen aan student
        nieuwe_klas = input("Geef de nieuwe klas: ")
        studenten[student_nummer][1] = nieuwe_klas
    else:
        print("ongeldige student nummer")

def verander_woonplaats_van_student():
    # welke student
    toon_alle_namen()
    student_nummer = int(input("Geef de nummer van de student: "))
    if student_nummer < len(studenten):
        # nieuwe woonplaats toevoegen vragen welke nieuwe en koppelen aan student
        nieuwe_woonplaats = input("Geef de nieuwe woonplaats: ")
        studenten[student_nummer][2] = nieuwe_woonplaats
    else:
        print("ongeldige student nummer")

# een lijst heeft als default behaviour het sorteren op level 0 in de lijst,
# maar wil je sorteren op een andere level dan moet een functie toevoegen

def sorteer_studenten_op_naam():
    # mijn studenten en mijn sorteer sleutel, teruggeven als resultaat
    res = sorted(studenten, key=lambda x: x[1])
    print(tabulate(res, headers=headers))



