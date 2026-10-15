# van teken naar ascii

teken = "V"

print(ord(teken))

# tekens ophalen is alt+64 = @

# van ascii naar teken
nummer = 64

print(chr(nummer))


# tekst => omzetten naar ascii waarden

tekst = "dit is een tekst omgezet naar ascii"
ascii_lijst = []

for teken in tekst:                    # elk teken van de string, één voor één
    ascii_lijst.append(ord(teken))     # omzetten naar een getal en achteraan toevoegen

print(*ascii_lijst)   # ik vergeet altijd de astrix erbij te zetten

for nummer in ascii_lijst:
    print(chr(nummer), end=" ")
print("")

# hoe kan ik dit versleutelen

tekst = "dit is een tekst omgezet naar ascii"
sleutel = 3                                  # hoeveel posities we opschuiven

versleuteld = ""                             # lege string, we bouwen die stap voor stap op
for teken in tekst:
    nieuw_getal = ord(teken) + sleutel       # teken -> getal, daarna opschuiven
    versleuteld += chr(nieuw_getal)          # getal -> teken, achteraan toevoegen

print(versleuteld)                           # glw#lv#hhq#...

# hoe kan ik dit ontcijferen

ontcijferd = ""
for teken in versleuteld:
    oud_getal = ord(teken) - sleutel         # nu terug opschuiven: min in plaats van plus
    ontcijferd += chr(oud_getal)

print(ontcijferd)                            # dit is een tekst omgezet naar ascii


# binair is een string en kan niet omgezet worden naar getal



