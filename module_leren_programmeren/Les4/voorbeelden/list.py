steden = ["rome", "parijs", "london", "madrid", "brussel"]
print(steden)
print(*steden)
print(steden[0])
print(steden[1])
print(steden[2])

"""for stad in range(5):
    print(steden[stad])"""

# index = plaats van de record in de array
# value = waarde van de recode in de array

"""for stad in steden:
    print(stad)"""

"""lotto_cijfers = [5,10,15,20,22,33,49]

for cijfer in lotto_cijfers:
    print(cijfer)"""

# toevoegen van een record

"""print("voor")
steden.append("genk")
print("na")
for stad in steden:
    print(stad)"""

# verschil tussen append en insert

# append achteraan bij zetten
# insert is op een bepaalde plaats zetten

steden.insert(2,"hasselt")
print("insert")
for stad in steden:
    print(stad, end ="\t")

# aanpassen van een value

"""steden [0] = "milaan"
print("na aanpassing")
for stad in steden:
    print(stad, end="\t")"""

# => bovenstaande is de volgorde CREATE - UPDATE - READ - DELETE

# verwijderen (is een examen vraag)
# verwijderen op value
print("")
print("na verwijderen op value")
steden.remove("hasselt")
for stad in steden:
    print(stad, end="\t")

# verwijderen op basis van index
print("")
print("na verwijderen op index")
steden.pop(2) #POP leeg dan gaat het systeem de laatste eruit halen = LIFO
for stad in steden:
    print(stad, end="\t")

steden.clear()
print("na clear")
del steden
print ("na del")
