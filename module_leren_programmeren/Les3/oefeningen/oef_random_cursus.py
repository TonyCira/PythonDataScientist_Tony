import random as rnd

#Schrijf een programma dat 3 random getallen optelt.

print(rnd.random()+rnd.random()+rnd.random()+rnd.random())

#Schrijf een programma dat een random getal genereert tussen 25 en 50

print((rnd.random()*26)+25)

#Schrijf een programma dat een random getal geneert tussen 13.7 en 19.8

print(rnd.uniform(13.7,19.8))

#Schrijf een programma dat 2 getallen geneneert a en b tussen 0-6 : a is groter, b is groter of a en b zijn even groot

a = print((rnd.random()*6)+0)
b = print((rnd.random()*6)+0)

if a == b:
    print(f"{a} is gelijk aan {b}")
elif a > b:
    print(f"{a} is groter dan {b}")
else :
    print(f"{b} is groter dan {a}")


