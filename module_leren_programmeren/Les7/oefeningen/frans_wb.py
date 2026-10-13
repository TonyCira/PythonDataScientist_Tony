import random as rnd

woordenboek = {"hallo":"bonjour", "geel":"jaune", "appel":"pomme", "hond":"chien"}

def toon_woordenboek():
    for nl,fr  in woordenboek.items():
        print(nl,fr)


def voeg_woord_toe():
    ned = input("geef het Nederlandse woord: ")
    fra = input("geef het Franse woord: ")
    woordenboek[ned]=fra

def zoek_woord():
    zoekwoord = input("geef het woord dat je wenst te zoekt: ").capitalize()
    if zoekwoord in woordenboek.keys():
        print(f"de vertaling van {zoekwoord} : {woordenboek[zoekwoord]} ")

    else:
        print("woord niet gevonden")


def verwijder_woord():
    zoek_woord = input("welke woord wil je verwijderen: ").capitalize()
    if zoek_woord in woordenboek.keys():
        woordenboek.pop(zoek_woord)
        print(f"{zoek_woord} is verwijderd")
    else:
        print("woord niet gevonden")

# 1 functie, pas vertaling aan
def wijzig_woord():
    zoek_woord = input("welke woord wil je wijzigen: ").capitalize()
    if zoek_woord in woordenboek.key():
        nieuwe_vertaling = input("geef de nieuwe Franse vertaling: ").capitalize()
        woordenboek[zoek_woord] = nieuwe_vertaling
        print(f"{zoek_woord} is aangepast naar {nieuwe_vertaling}")

    else:
        print("woord niet gevonden")

def oefen():
    aantal = min(3, len(woordenboek.keys()))
    woordenboek = rnd.sample(list(woordenboek.keys()), aantal)
    score = 0

    for nl in woordenboek:
        antwoord = input("wat is de franse vertaling van '{nl}? ").capitalize()
        if antwoord == woordenboek[nl]:
            print("juist!")
            score += 1
        else :
            print(f"fout, het juiste antwoord is: {woordenboek[nl]} ")

    print (f"je score: {score} op {aantal} ")


def toon_menu():
    print("1: toon het woordenboek")
    print("2: voeg een woord toe")
    print("3: zoek een woord")
    print("4: verwijder een woord")
    print("5: wijzig een vertaling")
    print("6: oefen")
    print("stop: stop het programma")

##### hoofdprogramma #####


toon_menu()
keuze = input("Maak je keuze: ").lower()

while keuze != "stop":
    if keuze == "1":
        toon_woordenboek()
    elif keuze == "2":
        voeg_woord_toe()
    elif keuze == "3":
        zoek_woord()
    elif keuze == "4":
        verwijder_woord()
    elif keuze == "5":
        wijzig_woord()
    elif keuze == "6":
        oefen()
    else:
        print("Verkeerde invoer")

    toon_menu()
    keuze = input("Maak je keuze: ").lower()

print("Tot ziens!")


