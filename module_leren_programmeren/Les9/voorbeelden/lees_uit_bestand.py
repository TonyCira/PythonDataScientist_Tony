bestand = open("tekst.txt", "r")

tekst = bestand.read()
print("")
print(tekst)

lijnen = tekst.split(",")
print(lijnen)

for e, naam in enumerate(lijnen):
    print(e ,naam)