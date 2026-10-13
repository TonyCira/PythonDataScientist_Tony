# een set is van belang om unieke waarden terug te geven
# een set heeft geen key of index, dus geen sortering
# set is aanpasbaar
# niet geordend

import random as rnd

munten = {"euro", "dollar", "pond", "euro", "euro", "yenn"}
munten.add("lira")
print(munten)

for munt in munten:
    print(munt)

# nut van een set
getallen = []
for i in range(50):
    getallen.append(rnd.randint(1,30))

resultaat = set(getallen) # expliciete casting "list" naar "set"
print(resultaat)

jongens = ["Ben", "Mark", "Ben"]
meisjes = ["An", "Sofie", "An"]
jongens.extend(meisjes)
print(jongens)

jongens = {"Ben", "Mark", "Ben"}
meisjes = {"An", "Sofie", "An"}
jongens.update(meisjes)
print(jongens)

lijst_getallen = [1,5,3,1,3,5,5]
uniek_beschermd = tuple(set(lijst_getallen))
print(uniek_beschermd)



