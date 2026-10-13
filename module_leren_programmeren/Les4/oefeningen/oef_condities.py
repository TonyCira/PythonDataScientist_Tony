import random as rnd

# Schrijf een programma dat een getal * 3 blijft doen zolang kleiner dan 1000

"""getal = 10

while getal < 1000:
    getal = getal * 3
    print(getal)"""

# Schrijf een programma blijft optellen tot een ingegeven som bereikt is

som = int(input("tot welke som tellen"))
totaal = 0

while totaal < som:
    getal = 10
    totaal = totaal + getal
    print(f"Huidige totaal : {totaal}")

# Schrijf een programma om een random getal te raden tussen 1 en 10. Geef daarna het aantal pogingen. Zonder feedback

te_raden_getal = rnd.randint(1, 100)
aantal_kansen = 0
geraden = False

while geraden == False:
    gok = int(input("Raad een getal tussen 1 en 100: "))
    aantal_kansen += 1

    if gok < te_raden_getal:
        print("Groter!")
    elif gok > te_raden_getal:
        print("Kleiner!")
    else:
        geraden = True
        print(f"Juist geraden! Je had {aantal_kansen} kansen nodig.")