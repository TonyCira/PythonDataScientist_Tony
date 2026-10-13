import random

print(round(random.random(),0))
print(round(random.random(),2))

#random getal tussen 0 en 10
#random random heeft geen parameters nodig

print(random.random()*11)
print(int(random.random()*11))

#random getal tussen 5 en 15

print((random.random()*11)+5)

#random tussen 9 en 16
# 7 is de range want je vraagt tss 9 en 16 , dus 16-9=7
# 9 is het begin van de range
print(int(random.random()*7)+9)

#random tussen -10 en 15
print(int(random.random()*25)-10)

#random 0 en 30, enkel even getallen (zonder if)
print(int(random.random()*16)*2)

