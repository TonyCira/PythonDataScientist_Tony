from operator import truediv

print(11//2)
print(10//2)
# impliciet : python bepaalt zelf welke type het teruggeeft
# expliciet : user vraagt uitdrukkelijk welk type terug te geven

x = 7

if x == 5 :
    print("x is 5")

else :
    print("x is niet 5")


y = 7

if y < 10:
    print("kleiner dan 10")

elif x < 100:
    print("10 of kleiner dan 100")
else:
    print("het is 100 of groter")


# for  loop weten hoeveel keer, x-aantal keer
# while voorwaarde dat voldaan moet worden

getal = 8

for i in range(100): # 0 tot en met 99
    print(getal)

for i in range(1,101): # 1 tot en met 100
    print(getal)

for i in range(1,101,5): # 1 tot en met 100 in stappen met 5
    print(getal)



tekst = "dit is een tekst die ik ga doorlopen"
for teken in tekst:
    print(teken)


getal = 0
while getal < 100:
    nieuw = int(input("geef een getal: "))
    getal += nieuw

print("de uitkomst is nu groter dan 100")

# functies

def zet_tekst_in_hoofdletters():
    tekst = input("geef tekst")
    tekst = tekst.upper()
    print(tekst)

zet_tekst_in_hoofdletters()

#### data zit niet in de functie maar moet uit het programma komen
def zet_tekst_in_hoofdletters(tekst): #
    tekst = tekst.upper()
    print(tekst)

#### hoofdprogramma ####

tekst_hfd = input("geef tekst")
zet_tekst_in_hoofdletters(tekst_hfd)

# hier moeten we consistent, input in functies of input via hoofdprogramma
# moeten even zien waar ik best mee om kan, ik wil consitent zijn met data op te vragen in de functies
# want ik wil geen vergissing maken, dus alle input nodig om de functie te doen werken de input via de functie te laten komen

# return is voor de data verder te gebruiken inplaats van de zien
# met print kan je debuggen als functies return hebben om data op te slaan
# print = laat zien
# return = onthou data

import random as appel

print(appel.random()) # pure vorm 0-1
print(appel.randint(1,10)) # geheel getal
print(appel.uniform(1,10)) # decimale
print(round(appel.uniform(1,10)),2) # decimale met afronding van 2 cijfers na de komma


# lambda

y= lambda x: x**2+x+5

print(y(2))

for i in range(-10,10):
    print(y(1))


# list met []
# index value principe, dus geordende + aanpasbaar

import random

lotto_cijfers = []

for i in range(7):
    getal = random.randint(1,45)
    lotto_cijfers.append(getal)

lotto_cijfers.sort() # van a tot z
lotto_cijfers.sort(reverse=True) # van z tot a
print(*lotto_cijfers)

# list met () = tuple
# index value principe, dus geordende + niet aanpasbaar (maar wel als je dit naar lijst zet en daarna terug naar

getallen = (5,9,2,1)

print(type(getallen))


# functie voor toevoegen = append(1 item) of extend (lijsttype)
# verwijderen = pop(index) , remove (value)
# index = geeft de eerste index van value (x)

eetdag = ["pizza", "kebab", "frieten", "pizza"]
print(eetdag.count("pizza"))
print(eetdag.count("kebab"))


#dictionary {key:value}
# key-value # key is uniek

auto1 = {"merk": "BMW", "model":"3-reeks", "bouwjaar":2025}
auto2 = {"merk": "BMW", "model":"5-reeks", "bouwjaar":2025}

wagen_park = {"Mark":auto1, "Dirk":auto2}

for kenmerk in auto1:
    print(kenmerk)

for kenmerk_K, kenmerk_V in auto1.items():
    print(kenmerk_K, kenmerk_V)

for persoon,auto in wagen_park.items():
    print("----------------")
    print(persoon,auto)
    print("----------------")
    for kenmerk in auto.values():
        print(kenmerk)

# toevoegen in een dictionary
# dictionary ["key"] = value of dictionay.update
wagen_park["hans"] = {"merk": "BMW", "model":"3-reeks", "bouwjaar":2026}
print(wagen_park)

# hoe in een functie gebruiken

def nieuwe_eigen_wagen():
    naam_eigenaar = input("geef de naam")
    merk = input("geef het merk")
    model = input("wat is het model")
    bouwjaar = input("wat is het bouwjaar")
    wagen_park[naam_eigenaar] = {"merk":merk, "model": model, "bouwjaar":bouwjaar}


# enumerate opsomming van index en values

namen = ["jan", "piet", "klaas"]

for key,value in enumerate(namen):
    print(key,value)


# list = aanpasbaar  , gesorteerd daar er een key is, dubbels mogelijk
# Dictionary = aanpasbaar, gesorteerd daar er een key is, dubbels mogelijk
# Tuple = niet aanpasbaar, gesorteerd daar er een key is, dubbels mogelijk
# Set = aanpasbaar, geen sortering daar er geen key is, geen dubbels mogelijk

# tuple en set zijn het tegenovergesteld van elkaar
# complementair

# set = data is uniek
# data uniek en niet aanpasbaar : tuple(set(data))



