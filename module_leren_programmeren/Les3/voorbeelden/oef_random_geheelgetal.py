import random as rnd # alias geven aan de import , shift+F6 pas alle aliassen aan in de file voor Pycharm


laagste = int(input("geef een laagste"))
hoogste = int(input("geef een hoogste"))

#indien gebruiker eerst een klein getal ingeeft en dan groot
if laagste < hoogste:
    print(rnd.randint(laagste,hoogste))

#indien gebruiker eerst een groot getal ingeeft
else :
    print(rnd.randint(hoogste,laagste))


