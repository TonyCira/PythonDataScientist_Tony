woordenboek={"kat":"cat", "hond" : "dog", "vis" : "fish"}

print(woordenboek["kat"]) # single de vertaling laten zien

print(*woordenboek.keys()) # de keys te zien

print(*woordenboek.values())  # de waardes te zien

persoon = {"naam":"jan",
           "leeftijd":35,
           "geslacht":"man",
           "woonplaats":"genk"}

print(persoon["naam"],persoon["leeftijd"])


for item in persoon.values():
    print(item)



# toont zowel de keys als values in een dictionary
# for loop voor zowel keys als values

persoon["hobby"] = "voetbal"
persoon.update({"job":"it", "salaris":4500})


for k,v in persoon.items():
    print(k,v)


for k,v in persoon.items():
    print(k,v)