import random as rnd

#Voorzie een lijst met personen. Zorg ervoor dat er een persoon toegevoegd, of verwijderd kan worden.

"""personen = ["pers1", "pers2", "pers3", "pers4"]

print(personen)
actie = input("wat wil je doen, persoon toevoegen of verwijderen? T of V").upper()
print(repr(actie))

if actie == "T" :
    persoon = (input("Welke persoon wil je toevoegen"))
    personen.append(persoon)
    print(personen)
elif actie == "V":
    persoon = (input("Welke persoon wil je verwijderen"))
    personen.remove(persoon)
    print(personen)
else :
    print(personen)
"""

#Voorzie een lijst met 7 willekeurige getallen tussen 15.9 en 75.48. Wat is de som van de lijst

"""getallen = [round(rnd.uniform(15.90, 75.48),2) for i in range(7)]
print(getallen)

som = sum(getallen)
print(f"de som is {som}")"""


#Voorzie een lijst met 20 willekeurige getallen tussen 10 en 200. Wat is het grootste en kleinste getal

getallen = [rnd.randint(10,200) for i in range(20)]
print(getallen)
print(min(getallen))
print(max(getallen))