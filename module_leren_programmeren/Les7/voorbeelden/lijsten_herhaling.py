import random as rnd


getallen= []

for i in range(10):
    getallen.append(rnd.randrange(1,200))

print(getallen)

y = lambda x : x*2+5 if x%2==0 else x*2

for i in range(len(getallen)):
    getallen[i] = y(getallen[i])

print(getallen)



