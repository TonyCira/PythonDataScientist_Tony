from tabulate import tabulate

koppen = ["naam", "gemeente", "leeftijd"]

personen =[
    ["Jan", "Hasselt", 35],
    ["Piet", "Genk", 28],
    ["Julie", "Genk", 24],
    ["Amber", "As", 30],
    ["louise", "Lommel", 31]
]

# toon index en data

"""def toon_data():
    print("index, naam, gemeente, leeftijd")
    for index, persoon in enumerate (personen):
        print(index, *persoon)"""


# voeg een persoon toe Persoon = list toevoegen

"""def voeg_persoon_toe():
    naam = input("naam: ").capitalize()
    gemeente = input("gemeente: ").capitalize()
    leeftijd = input("leeftijd: ")

    persoon = [naam, gemeente, leeftijd]
    # personen.extend(persoon) # ieder index krijgt  5 T o n y - 6 D i e p e n b e e k - 7 4 8
    personen.append(persoon)
    # personen.append(naam, gemeente, leeftijd) is ook een schrijfwijze om te gebruiken

voeg_persoon_toe()
toon_data()"""


# toon namen
"""
def toon_namen():
    for naam in personen:
        print(naam)"""

"""toon_namen()"""

# komt naam voor in de lijst:

#manier 1
"""def zoek_naam_persoon_1():
    zoek_naam1 = input("te zoeken naam: ").capitalize()
    for naam in personen:
        if naam [0] == zoek_naam1:
            print("gevonden")
        else:
            print("niet gevonden")"""

# manier 2

"""def zoek_naam_persoon_2():
    zoek_naam2 = input("te zoeken naam: ").capitalize()
    if zoek_naam2 in toon_namen():
        print("gevonden")
    else:
        print("niet gevonden")


zoek_naam_persoon_1()
zoek_naam_persoon_2()"""

#verwijder persoon

"""def verwijder_persoon():
    toon_data()
    nummer = int(input("nummer die je wilt verwijderen: "))
    if nummer < len(personen):
        personen.pop(nummer)
        print("persoon is verwijderd")
    else:
        print("ongeldig nummer")

toon_namen()
verwijder_persoon()"""


# toon_data in tabel

def toon_data_als_tabel():
    # tabel = tabulate(personen, headers=koppen, tablefmt="fancy_grid")
    tabel = tabulate(personen, headers=koppen, tablefmt="html")
    print(tabel)

toon_data_als_tabel()





