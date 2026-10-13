# for loop = aantal keer aangegeven en loop stopt

# while loop = voorwaarden voldoet blijft de loop lopen

# for voorbeelden

"""getal= 7

for i in range(1,11):
    print(f"{getal} x {i} = {getal*i}")"""


#schrijf straf 200 keer

tekst = "ik zal braaf zijn en naar de leerkracht luisteren"

# mogelijkheid 1
"""for i in range(1,201):
    print(tekst)"""

# mogelijkheid 2
"""for i in range(200): #0-199
    print(tekst)"""

# mogelijkheid 3
"""aantal = 200    

for i in range(aantal):
    print(tekst)"""

# mogelijkheid 4

"""aantal  = 100
bereik = range(5,105) # van tot
for i in bereik:
    print(i)"""

# mogelijkheid 5

"""aantal  = 100
bereik = range(5,105,5) # interval
for i in bereik:
    print(i)"""

# mogelijkheid 6

"""aantal  = 100
bereik = range(105,5,-1) # aftellen
for i in bereik:
    print(i)"""

# tafelkaar in tabel laten zien

for i in range(1,11): # rijen aanmaken met de formule
    for j in range(1,11): # kolomen aanmaken met de formule
        print(i*j, end = "\t")
    print("")

# voor 3D moet je een derde for zetten voor de diepte
