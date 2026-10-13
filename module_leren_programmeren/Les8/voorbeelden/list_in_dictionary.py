# list van dictionaries, die een list bevat

persoon_1 = {"naam" : "geert", "leeftijd":40, "hobbies":["voetbal", "wielrennen","sportkrant lezen"]}

print(persoon_1)

for k, v in persoon_1.items():
    print(k,v)

for hobby in persoon_1["hobbies"]:
        print(hobby)


for k, v in persoon_1.items():
    print(k,v)
    for hobby in persoon_1["hobbies"]:
        print(hobby)


def toon_info():
    print(f"naam: {persoon_1["naam"]}")
    print(f"leeftijd: {persoon_1["leeftijd"]}")
    for hobby in persoon_1["hobbies"]:
        print(hobby, end ="\t")
    print("")
    print("------")


toon_info()


persoon_1 = {"naam" : "geert", "leeftijd":40, "hobbies":["voetbal", "wielrennen","sportkrant lezen"]}
persoon_2 = {"naam" : "gert", "leeftijd":45, "hobbies":["voetbal", "reizen"]}
persoon_3 = {"naam" : "valerie", "leeftijd":30, "hobbies":["lezen", "reizen","paard rijden"]}
persoon_4 = {"naam" : "peter", "leeftijd":16, "hobbies":"gamen"}

lijst_personen =[persoon_1, persoon_2, persoon_3, persoon_4]

def toon_info():
    for e,persoon in enumerate(lijst_personen):
        print(f"lijstnummer {e}")
        print(f"naam: {persoon["naam"]}")
        print(f"leeftijd: {persoon["leeftijd"]}")
    for hobby in persoon["hobbies"]:
        print(hobby, end ="\t")
    print("")
    print("------")

def toon_naam_nummer():
    for e,persoon in enumerate(lijst_personen):
        print(e, persoon["naam"])

def voeg_persoon_toe():
    naam = input('geef naam van persoon')
    leeftijd = int(input('geef leeftijd van persoon'))
    hobbies = [] # een lege lijst, want bij aanmaken nog geen gekende hobbies
    lijst_personen.append({"naam":naam, "leeftijd":leeftijd, "hobbies":hobbies})

def voeg_hobby_toe_aan_persoon():
    #wie en wat
    toon_naam_nummer()
    nummer = int(input("welke nummer wil je aanspreken")) # wie
    if nummer > len(lijst_personen):
        print("ongeldig nummer")
    else:
        hobby = input("geef de hobby van de persoon")
        lijst_personen[nummer]["hobbies"].append(hobby)

def verwijderen_een_persoon():
    #wie moet verwijdert worden, index
    toon_naam_nummer()
    nummer = int(input("geef nummer van persoon die wilt verwijderen"))
    #op lijst niveau moet de persoon verwijdert worden
    if nummer < len(lijst_personen):
        lijst_personen.pop(nummer)
    else:
        print("ongeldige nummer")


#voeg_persoon_toe()
#voeg_hobby_toe_aan_persoon()
verwijderen_een_persoon()
toon_info()
#toon_naam_nummer()