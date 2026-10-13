import random as rnd

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
