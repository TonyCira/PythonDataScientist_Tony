import math

# Maak een deelprogramma dat de deling en rest terug geeft 19/3 = 6 rest 1

"""getal = 19
deler = 3
print(f"{int(getal/deler)} rest {getal%deler}")"""

# Schrijf een programma dat de omtrek van een cirkel berekent

"""d=3
cirkel = d * math.pi
print(int(cirkel))"""

# Schrijf een programma dat de oppervlakte van een kubus berekent

"""z=3
oppv = 6 * math.pow(z,2)
print (f"een kubus heeft een oppervlakte {int(oppv)}")"""

# Schrijf een programma dat de inhoud van een balk berekent dat voor x procent gevuld is

"""vulperc = 50
b,h,l = 5,5,5
print((b*h*l)*50/100)"""

# Schrijf een programma dat graden °c omzet naar °f

"""c=30
omz = (c * 1.8) + 32
print(omz)"""


# Schrijf een programma dat het aantal graden van een n hoek berekent = (n-2)*180

"""n = 5
hoek = (n-2)*180
print(hoek)
"""

"""Oefeningen if statement"""

# Controleer of een getal deelbaar is door 7

"""getal = 15

if getal % 7 == 0:
    print("getal is deelbaar door 7")
else:
    print("getal is niet deelbaar door 7")"""

# Geef 2 getallen in. Het programma zegt getal a is groter dan, kleiner dan, even groot.

"""a = int(input("geef een getal"))
b = int(input("geef een getal"))

if a == b:
    print("getal is even groot")
elif a<b:
    print(f"{a} is kleiner dan {b}")
else :
    print(f"{a} is groter dan {b}")"""

# Geef een getal in: indien het even is doe het getal maal 2 anders / 2

"""a = int(input("geef een getal"))

if a % 2 == 0 :
    print(f"getal is even, {a} maal 2 = {a*2}")
else :
    print(f"getal is oneven, {a} delen 2 = {a/2}")"""

# Schrijf een programma dat weergeeft welk soort hoek, stomp, recht of scherp

"""a = int(input("geef de graden van de hoek"))

if a < 90 :
    print("dit is een scherpe hoek")
elif a == 90 :
    print("dit is een rechte hoek")
elif a < 180 :  # niet nodig een "> 90" erbij te zetten want de eerste twee hebben dit reeds gedaan
    print("dit is een stompe hoek")
elif a == 180 :
    print("dit is een gestrekte hoek")
else :
    print("dit is geen hoek meer")"""


"""Gevorderde"""

# Schrijf een programma dat (a+b)² kan uitrekenen

"""a = float(input("geef een getal"))
b = float(input("geef een getal"))

kwadraat = (a+b)**2

print(f"de macht van {a} + {b} = {kwadraat}")"""

# Schrijf een programma dat de schuine zijde van een rechthoek berekent. Pythogras
# Schuine zijde van een rechthoekige driehoek — stelling van Pythagoras
# c² = a² + b²

"""a = float(input("geef een getal"))
b = float(input("geef een getal"))

pyth = math.sqrt(a**2 + b**2)

print(f"de schuine zijde van een rechthoek van {a} + {b} = {round(pyth,2)}")"""

# Schrijf een programma dat de oppervlakte van een vijfhoek berekent

"""a = float(input("geef een getal"))

oppv = (5/4) * (a**2) * (1 / math.tan(math.pi/5))

print(f"Oppervlakte van een regelmatige vijfhoek met {a} als zijde = {round(oppv,2)}")"""


# Schrijf een programma dat berekent hoeveel 1cm² pizza kost(diameter, prijs)
# Oppervlakte cirkel = π × straal²   (straal = diameter / 2)
# prijs_per_cm2 = totaalprijs / oppervlakte

"""dia = float(input("geef de diameter van de pizza"))
prijs = float(input("hoeveel kost de pizza"))

pizza = math.pi * (dia/2)**2

print(f"de prijs per vierkante cm van uw pizza is {round(prijs/pizza,2)}")"""


# Schrijf een programma dat eenheden, tientallen en hondertallen,duizentallen scheidt 1123= 1d, 1h, 2t, 3e

"""getal = int(input("geef een getal"))

print(f"{(getal // 1000) % 10}d,{(getal // 100) % 10}h,{(getal // 10) % 10}t,{getal % 10}e")"""

# Schrijf een programma dat volgende boodschap geeft <0(negatief) <10 <100 <1000 <10000

"""a = int(input("geef een getal"))

if a <0 :
    print("getal is negatief")
elif a < 10:
    print("getal is kleiner dan 10")
elif a < 100:
    print("getal is kleiner dan 100")
elif a < 1000:
    print("getal is kleiner dan 1000")
elif a < 10000:
    print("getal is kleiner dan 10000")
else :
    print("getal is groter dan 10000")"""

