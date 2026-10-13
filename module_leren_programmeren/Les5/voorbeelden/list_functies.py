    #      0     1        2       9
namen = ["An","Ben","Cedric", "Dana"]

print(namen[-1])

def toon_namen():
    for naam in namen:
        print(naam)

def voeg_naam_toe():
    naam = input("geef de naam van de persoon ")
    namen.append(naam.capitalize())
    print(f"{naam} toegevoegd aan lijst")

def bestaat_de_naam():
    naam = input("geef een naam en kijk of wezig in de lijst ")
    if naam in namen:
        print(f"{naam} is in de lijst")
    else :
        print(f"{naam} is niet in de lijst")

def verwijder_personen():
    naam = input("geef de naam van de persoon die je wilt verwijderen").capitalize()
    if naam in namen:
        namen.remove(naam)
        print(f"{naam} is verwijdert uit de lijst")
    else:
        print(f"{naam} niet gevonden")

def functies():
    print("1: toon de namen")
    print("2: naam is toegevoegd")
    print("3: is de naam in lijst")
    print("4: naam is verwijdert")
    print("stop : stop het programma")

#####  hoofdprogramma   ######

functies()
keuze = input("maak je keuze ")
while keuze.lower != "stop" :
    if keuze == "1":
        toon_namen()
    elif keuze == "2":
        voeg_naam_toe()
    elif keuze == "3":
        bestaat_de_naam()
    elif keuze == "4":
        verwijder_personen()
    else:
        print("verkeerde invoer")

    functies()
    keuze = input("maak je keuze ")

