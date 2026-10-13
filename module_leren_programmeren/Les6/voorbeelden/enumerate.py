# ENUM'S

plaatsen = ["Parijs", "Rome", "Madrid", "Milaan"]

#hoe we het nu kennen
for plaats in plaatsen:
    print(plaats)

# Enumerate = FOR loop waarmee we de index en value van de lijst krijgen.

for index, plaats in enumerate(plaatsen): #start standaard bij nul
    print(index, plaats)

for index, plaats in enumerate(plaatsen, start=1): #start nummering zelf bepalen
    print(index, plaats)



