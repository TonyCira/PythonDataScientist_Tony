# = is een waarde toekennen
# == is een waarde vergelijken uitkomst is enkel TRUE or FALSE

"""getal = 5
print(getal == 5)
print(getal == 7)

# if functie met 2 opties
if getal == 5:
    print("getal is 5")
else :
    print("getal is niet 5")"""

# if functie met meer opties

"""getal = 7
if getal == 5:
    print("getal is 5")
elif getal < 5:
    print("getal is kleiner dan 5")
else:
    print("getal is groter dan 5")"""

# is een getal <100, kleiner <10 of groter dan 100

"""getal = 5

if getal < 100:
    print("getal is kleiner dan 100")
elif getal < 10 :
    print("getal is kleiner 10")
else :
    print("getal is 100 of groter")"""

"""getal = 1100
if getal < 10:
    print("kleiner dan 10")
if getal > 10:
    print("groter dan 10")
if getal > 100:
    print("groter dan 100")
if getal > 1000:
    print("groter dan 1000")"""

#alles behalve, niet "!="

"""getal = 65
if getal != 5:
    print("getal is niet 5")
else:
    print("getal is 5")"""

# <3 jaar baby, <10j kind, <18 tiener, 18+ volwassen

leeftijd = 3

if leeftijd <= 3:
    print("baby")
elif leeftijd < 10 :
    print("kind")
elif leeftijd < 18:
    print("tiener")
else:
    print("Volwassen")

