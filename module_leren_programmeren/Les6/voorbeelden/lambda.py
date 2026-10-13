import math

#### Functies ######

x = lambda a : a + 10
# z = 2x + y
z = lambda x, y : 2*x+y

#X,Y = x²+y+5

oef_1 = lambda x, y: x*x+y+5
print(oef_1(1, 2))

#X,y = (x+y)²

oef_2 = lambda x, y: (x+y)**2

#X,y,z = x²+z*y+x+5

oef_3 = lambda x, y, z: x*x + z * y + x + 5

#X,y = if x > y, x*2 else x/2

oef_4 = lambda x, y: x*2 if x>y else x/2

#X,y if x*2 > y, x/2 else y*2

oef_5 = lambda x, y: x*2 if x>y else x/2

#### Hoofdprogramma ######

print(oef_5(1, 2))
