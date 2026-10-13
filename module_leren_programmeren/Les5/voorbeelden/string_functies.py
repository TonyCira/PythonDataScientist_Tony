tekst = "dit is een stukje tekst"
print(len(tekst)) # geef de lengte van de tekst
print(tekst[0])

# hoe spel ik een string. kip = KIP

"""for i in range (len(tekst)):
    print(tekst[i], end=" ")

for teken in tekst:
    print(teken, end=" ")"""


voornaam = "Tony"
familienaam = "Cirafici"
init = voornaam[0:2]+ familienaam[0:2]
print(init)

print(tekst[::-1]) # draait te tekst om (van het begin naar het einde)

print(tekst.upper())
print(tekst.lower())
print(tekst.title())
print(tekst.capitalize())

namen = ["An", "Anne", "Berta","Celien", "Amber"]
naam = "An"
"""print(naam.startswith("A"))"""

def toon_namen_begint_met_letter():
    # toont enkel de namen met de letter()

    beginletter=input("geef beginletter ").upper()
    result = []

    for naam in namen:
        if naam.startswith(beginletter):
            result.append(naam)
        print(*result)

# toon_namen_begint_met_letter()

woord="dolfijnen"

print(woord.find("n"))
print(woord.index("n"))
print(woord.index("e"))

print(woord.replace("j", "1"))




