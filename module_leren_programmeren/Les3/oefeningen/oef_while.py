import random as rnd

#Schrijf een programma dat een getal 10 keer vermenigdvuldigt.

"""getal = int(input("Geef een getal: "))
teller = 1

while teller <= 10:
    print(f"{getal} x {teller} = {getal * teller}")
    teller += 1"""

#Schrijf een programma dat 10 random getallen tussen 1 en 20 geeft

"""teller = 0
while teller < 10:
    getal = rnd.randint(1, 20)
    print(getal)
    teller += 1"""


#Schrijf een programma raad het getal tussen 1 en 100. Geef feedback, groter, kleiner,
# juist geraden. Aantal raadkansen + in hoeveel kansen geraden


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