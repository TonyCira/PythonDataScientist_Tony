#Maak volgend patroon
#Vierkant
"""
####
####
####
####
"""

"""for i in range(4):
    print("####")"""



#Maak volgend patroon
#rechthoek
"""
#####
#####
#####
#####
"""

"""for i in range(4):
    print("#####")
"""


#Hoeveel rijen en hoeveel kolommen
"""
#####
$$$$$$$
#####
$$$$$$$
#####
"""

"""for i in range(5):
    if i % 2 == 0:
        print("$$$$$$$")
    else :
        print("#####")"""

#Vraag aan gebruiker de 2 tekens
"""
#####
$$$$$$$
#####
$$$$$$$
#####
"""

"""teken1 = input("geef het eerste teken (voor de rijen van 5 ): ")
teken2 = input("geef het eerste teken (voor de rijen van 7 ): ")

for i in range (5):
    if i % 2 == 0:
        print(teken1 * 5)
    else:
        print(teken2 * 7)"""


# patroon maken
"""
xxx
yyy
zzz
Xxx
yyy
zzz
"""

"""for i in range(6):
    if i % 3 == 0:
        print("xxx")
    elif i % 3 == 1:
        print("yyy")
    else:
        print("zzz")
"""
#Vraag aantal rijen

"""
#
##
###
#####
"""

"""aantal_rijen = int(input("hoeveel rijen wil je? "))

for i in range(aantal_rijen + 1):
    print("#" * i)"""

# Vraag aantal teken

"""
#
##
###
#####
###
##
#
"""

aantal_tekens = int(input("wat is het maximum aantal tekens? "))

for i in range(aantal_tekens + 1):
    print("#" * i)

for i in range(aantal_tekens -1, 0, -1):
    print("#" * i)