lijst_personen = [
    {"naam": "geert", "leeftijd": 40, "hobbies": ["voetbal", "wielrennen"]},
    {"naam": "gert",  "leeftijd": 45, "hobbies": ["voetbal", "reizen"]},
    {"naam": "mia",   "leeftijd": 30, "hobbies": ["lezen"]},
    {"naam": "peter", "leeftijd": 16, "hobbies": ["gamen"]},
]

def toon_info():
    for e, persoon in enumerate(lijst_personen):
        print(f"lijstnummer {e}")
        print(f"naam: {persoon['naam']}")
        print(f"leeftijd: {persoon['leeftijd']}")
    for hobby in persoon["hobbies"]:
        print(hobby, end="\t")
    print("")
    print("------")