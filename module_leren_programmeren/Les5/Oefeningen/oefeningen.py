import random as rnd

from module_leren_programmeren.Les1.voorbeelden.vb_1 import getal

#Maak lijst met bezochte plaatsen, zorg dat je plaats kan tonen, toevoegen, verwijderen, en opzoeken(bezocht, niet bezocht) optie controle hoofd/kleine letter

"""steden = ["Rome","Ibiza","Marseille","Brussel"]

def toon_steden():
    for stad in steden:
        print(stad)

def voeg_stad_toe():
    stad = input("geef een stad: ")
    steden.append(stad)
    print(f"{stad} toegevoegd aan de lijst")

def bestaat_de_stad():
    stad = input("geef een stad en kijk of aanwezig in de lijst")
    if stad in steden:
        print(f"{stad} is in de lijst")
    else:
        print(f"{stad} is niet in de lijst")

def verwijder_stad():
    stad = input("geef de stad die je wilt verwijderen")
    if stad in steden:
        steden.remove(stad)
        print(f"{stad} is verwijderd uit de lijst")
    else:
        print(f"{stad} niet gevonden")


def functies():
    print("1: toon de steden")
    print("2: voeg een stad toe")
    print("3: is de stad in de lijst")
    print("4: verwijder een stad uit de lijst")
    print("stop: stop het programma")

#######################HOOFDPROGRAMMA######################

functies()
keuze = input("maak je keuze: ")
while keuze != "stop":
    if keuze == "1":
        toon_steden()
    elif keuze == "2":
        voeg_stad_toe()
    elif keuze == "3":
        bestaat_de_stad()
    elif keuze == "4":
        verwijder_stad()

    functies()
    keuze = input("maak je keuze: ")"""


#Maak een functie die 2 lijsten samenvoegd. Deze geeft een lijst terug

"""def lijsten_samenvoegen(lijst1, lijst2):
    resultaat = lijst1 + lijst2
    return resultaat


# Voorbeeld van gebruik:
a = [1, 2, 3]
b = [4, 5, 6]
nieuwe_lijst = lijsten_samenvoegen(a, b)
print(nieuwe_lijst)"""

#Simuleer een kop of munt: vraag naar aantal keer,  steek alle waarde in een lijst, geef daarna % kop en % munt. pas naar aantal keer


"""
aantal_worpen = int(input("hoeveel keer wil je gooien: "))
resultaten = []

for i in range(aantal_worpen):
    worp = rnd.choice(["Kop", "Munt"])
    resultaten.append(worp)

aantal_kop = resultaten.count("Kop")
aantal_munt = resultaten.count("Munt")

percentage_kop = (aantal_kop / aantal_worpen) * 100
percentage_munt = (aantal_munt / aantal_worpen) * 100

print(resultaten)
print(f"Kop: {percentage_kop}%")
print(f"Munt: {percentage_munt}%")"""


#Maak een module wiskunde:
#Oppv_vierkant, oppv_rechthoek, oppv_cirkel. Inhoud_kubus, inhoud_balk, inhoud cilinder.
#Zorg voor een user interface.

#  ==> zie Wiskunde

#Test of een string een palindroom is. Lepel, kaak, racecar

"""def is_palindroom(tekst):
    tekst = tekst.lower()
    return tekst == tekst[::-1]

woord = input("geef een woord: ")
if is_palindroom(woord):
    print(f"{woord} is een palindroom.")
else :
    print(f"{woord} is geen palindroom.")"""



#Maak een functie dat het langste woord in een lijst terug geeft.

"""def langste_woord(lijst):
    langste = lijst[0]
    for woord in lijst:
        if len(woord) > len(langste):
            langste = woord
    return langste


woord_lijst = ["vul","peen", "stier"]
print(langste_woord(woord_lijst))"""


#Maak een functie kraak de code, hij heeft als feedback, goed, groter, kleiner per getal.

"""def kraak_de_code():
    code = rnd.randint(0,10)
    geraden = False

    while geraden == False:
        getal = int(input("geef een getal: "))

        if getal > code :
            print("kleiner")
        elif getal < code :
            print("groter")
        else:
            geraden = True
            print(f"{getal} kraakt de code")


kraak_de_code()"""

#Maak een programma dat rekenen sommen willekeurig genereerd. Sla de juist en foute op in 2 lijsten, juist of fout. Geef na een fout het juiste antwoord

"""import random as rnd

juist_lijst = []
fout_lijst = []

aantal_sommen = int(input("Hoeveel sommen wil je maken? "))

for i in range(aantal_sommen):
    getal_1 = rnd.randint(1, 20)
    getal_2 = rnd.randint(1, 20)
    operator = rnd.choice(["+", "-", "*"])

    if operator == "+":
        juist_antwoord = getal_1 + getal_2
    elif operator == "-":
        juist_antwoord = getal_1 - getal_2
    else:
        juist_antwoord = getal_1 * getal_2

    som_tekst = f"{getal_1} {operator} {getal_2}"
    antwoord = int(input(f"{som_tekst} = "))

    if antwoord == juist_antwoord:
        print("Juist!")
        juist_lijst.append(som_tekst)
    else:
        print(f"Fout! Het juiste antwoord was {juist_antwoord}.")
        fout_lijst.append(som_tekst)

print(f"Juiste sommen: {juist_lijst}")
print(f"Foute sommen: {fout_lijst}")"""

### Colorama oefening

#Vul een lijst met willekeurige getallen-50 tot 50. Positieve groen, Negatieve rood

"""from colorama import Fore
import random as rnd

getallen = [rnd.randint(-50, 50) for i in range(10)]

for getal in getallen:
    if getal > 0:
        print(Fore.GREEN + str(getal))
    elif getal < 0:
        print(Fore.RED + str(getal))
    else:
        print(getal)"""

#Pas die aan met zelf een gekozen waarde, indien het grote dan groen, anders geel.


#Maak een module tekst. Opmaak.
#Zet in groen
#Zet in rood en hoofdletters
#Zet in kleur(rood, blauw, groen, orange)

"""from colorama import Fore, Style

def zet_groen(tekst):
    return Fore.GREEN + tekst + Style.RESET_ALL

def zet_rood_hoofdletters(tekst):
    return Fore.RED + tekst.upper() + Style.RESET_ALL

def zet_kleur(tekst, kleur):
    if kleur == "rood":
        code = Fore.RED
    elif kleur == "blauw":
        code = Fore.BLUE
    elif kleur == "groen":
        code = Fore.GREEN
    elif kleur == "orange":
        code = "\033[38;5;208m"
    else:
        code = Style.RESET_ALL

    return code + tekst + Style.RESET_ALL


print(zet_groen("Dit is groen"))
print(zet_rood_hoofdletters("dit wordt rood en in hoofdletters"))
print(zet_kleur("Dit is blauw", "blauw"))
print(zet_kleur("Dit is oranje", "orange"))"""

## Herhaling if en while

#Maak een tekstbased game. Waarin de gebruiker keuzes kan maken.
#Altijd 2 of 3 keuze. Bij sommige gebruik je een while.
#Geef ook altijd een opdracht om terug naar de volgende vraag te gaan.

def keuze_vragen(prompt, geldige_keuzes):
    keuze = input(prompt)
    while keuze not in geldige_keuzes:
        print("Ongeldige keuze, probeer opnieuw.")
        keuze = input(prompt)
    return keuze


def start():
    print("\nJe staat aan het begin van een pad. Voor je zie je een donker bos en een klein dorp.")
    print("1: Ga naar het bos")
    print("2: Ga naar het dorp")
    keuze = keuze_vragen("Wat doe je? (1/2): ", ["1", "2"])

    if keuze == "1":
        bos()
    else:
        dorp()


def bos():
    print("\nIn het bos hoor je een geluid. Er staat een wolf voor je.")
    print("1: Vecht met de wolf")
    print("2: Klim in een boom")
    print("3: Ren terug naar het pad")
    keuze = keuze_vragen("Wat doe je? (1/2/3): ", ["1", "2", "3"])

    if keuze == "1":
        print("Je verliest het gevecht tegen de wolf. Game over.")
    elif keuze == "2":
        print("Je klimt veilig in de boom. De wolf loopt weg. Je wint!")
    else:
        print("Je rent terug naar het pad, veilig maar zonder avontuur.")


def dorp():
    print("\nHet dorp is stil. Een oude man biedt je een kaart aan.")
    print("1: Neem de kaart aan")
    print("2: Weiger en ga verder")
    keuze = keuze_vragen("Wat doe je? (1/2): ", ["1", "2"])

    if keuze == "1":
        print("Met de kaart vind je een schat. Je wint!")
    else:
        print("Je gaat verder zonder hulp. Het avontuur eindigt hier.")


start()



### Uitbreiding 1
#Maak een quiz met a b c d
#Geef feedback op de score
#Houd de antwoorden bij.



### Uitbreiding 2
#Galgje
#Kies een random woord uit een lijst van 10 tot 15 woorden.
#Je hebt 7 kansen
#Extra Uitbreiding. Teken een galg

import random as rnd

woorden = ["python", "computer", "programmeren", "functie", "variabele",
           "lijst", "toetsenbord", "scherm", "algoritme", "geheugen",
           "netwerk", "database"]

galg_tekeningen = [
    "\n \n \n \n \n \n---",
    "\n  O\n \n \n \n \n---",
    "\n  O\n  |\n \n \n \n---",
    "\n  O\n /|\n \n \n \n---",
    "\n  O\n /|\\\n \n \n \n---",
    "\n  O\n /|\\\n /\n \n \n---",
    "\n  O\n /|\\\n / \\\n \n \n---",
    "\n  X\n /|\\\n / \\\n(game over)\n \n---"
]


def toon_woord(woord, geraden_letters):
    weergave = ""
    for letter in woord:
        if letter in geraden_letters:
            weergave = weergave + letter + " "
        else:
            weergave = weergave + "_ "
    return weergave


def galgje():
    woord = rnd.choice(woorden)
    geraden_letters = []
    fouten = 0
    max_fouten = 7

    while fouten < max_fouten:
        print(galg_tekeningen[fouten])
        print(toon_woord(woord, geraden_letters))

        if "_" not in toon_woord(woord, geraden_letters):
            print("Proficiat, je hebt het woord geraden!")
            return

        letter = input("Geef een letter: ").lower()

        if letter in geraden_letters:
            print("Die letter had je al geprobeerd.")
        elif letter in woord:
            geraden_letters.append(letter)
        else:
            geraden_letters.append(letter)
            fouten += 1
            print("Foute letter!")

    print(galg_tekeningen[fouten])
    print(f"Game over! Het woord was: {woord}")


galgje()