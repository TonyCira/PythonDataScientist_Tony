import random as rnd

#Schrijf een programma dat een getal 10 keer vermenigdvuldigt.

"""aantal = 10
getal = int(input("geef een getal voor 10 keer te vermenigvuldigen"))

for i in range(1,aantal + 1):
    print(getal * i)"""

#Schrijf een programma dat 10 random getallen tussen 1 en 20 geeft. 

"""aantal = 10

for i in range(1,aantal + 1):
    getal = rnd.randint(1, 20) # binnen de lus zetten
    print(getal)
"""

# Maak een programma voor het oefenen van de maaltafels. Gebruiker geeft aan wat het hoogste getal is bvb 10 dan krijg hij 10 oefeningen:
# 5*7,9*3,2*2 deze worden random aangemaakt

aantal_oef = int(input("geef het aantal oefeningen dat je wil maken"))
score = 0

for i in range(1,aantal_oef+1):
    getal_1 = rnd.randint(1, 10)
    getal_2 = rnd.randint(1, 10)
    antwoord = int(input(f"{getal_1} * {getal_2} ="))

    if antwoord == getal_1 * getal_2:
        print(f"juist")
        score += 1
    else:
        print(f"Fout, juiste getal was {getal_1 * getal_2}")

print(f"Je had {score} van de {aantal_oef} oefeneningn juist ")

