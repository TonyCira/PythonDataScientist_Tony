bestand = open("tekst.txt", "a") # bestaat het bestand niet dan maakt het systeem dit zelf aan

# w = overschrijven
# a = toevoegen
# r = lezen
# x = aanmaken

bestand.write("Dit is een tekst" + "\n")

# hoe een lijst met items wegschrijven naar txt bestand

bestand = open("lijst_klas.txt", "a")

lijst_klas = ["Bjorn", "Tony", "Bart"]

for e, naam in enumerate(lijst_klas):
    bestand.write(str(e) + " " + naam + "\n")


