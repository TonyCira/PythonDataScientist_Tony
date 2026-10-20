fruits = ["apple", "banana", "cherry", "mango" ]
newlist = [x for x in fruits if "a" in x]

print(newlist)


import random as rnd
getallen = []

for _ in range(15):
    getallen.append(rnd.randint(0, 100))

print(*getallen)
newlist1 = sorted([x for x in getallen if x%2==0])
print(*newlist1)