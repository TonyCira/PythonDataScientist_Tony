"""som = 0

while som < 100:
    getal=int(input("geef een nieuw getal"))
    som  += getal
    print(som)

print("het getal is nu groter dan 100")"""

"""
tafel = 7

for i in range(100):
    print(tafel*i)

tafel = 7

for i in range(1,101):
        print(tafel * i)


tafel = 7

for i in range(1,101,5):
    print(tafel*i)"""

"""for i in range (1,11):
    for j in range (1,11):
        print(i*j, end="")
        print()
        print("-----------")"""

# vierkant
zijde = int(input("lengte van de zijde"))
teken = input("geef teken")
for i in range(zijde):
    for j in range (zijde):
        print (teken, end=" ")
        print()

# rechthoek

rijen = int(input("geef het aantal rijen"))
kolommen = int(input("geef het aantal kolommen"))
teken = input("geef teken")

for i in range(rijen):
    for j in range (kolommen):
        print (teken, end=" ")
        print()


