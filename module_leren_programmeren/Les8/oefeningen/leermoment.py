# vraag 1

x = 0

while x > 50:
    nieuw = int(input("geef een getal: "))
    x += nieuw

print("de uitkomst is nu groter dan 100")

# vraag 2

set = {4,2,4,9,2,1}

set.sort()
print(*set)

# vraag 3

# a

wagens = [
    {"eigenaar": "Mark", "merk": "BMW", "bouwjaar": 2025},
    {"eigenaar": "Dirk", "merk": "Audi", "bouwjaar": 2023},
    {"eigenaar": "Hans", "merk": "BMW", "bouwjaar": 2026},
]

def toon_wagens():
    for key, wagen in enumerate(wagens):
        print(f"{key,1}: {eigenaar} -  {merk} ({bouwjaar}")

# b

def voeg_wagen_toe():
    naam_eigenaar = input("geef eigenaar")
    merk = input("geef merk")
    bouwjaar = int(input("geef bouwjaar"))
    wagens = {"eigenaar":naam_eigenaar, "merk": merk, "bouwjaar":bouwjaar}

# c

merk = set(wagens)
