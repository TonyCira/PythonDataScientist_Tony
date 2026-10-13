import math

keuze = int(input("geef keuze"))

if keuze == 1:
    getal = int(input("geef een getal in"))
    if getal % 5 == 0:
        print (getal / 5)
    else:
        print (getal / 2)

elif keuze == 2:
    getal = int(input("geef een getal in"))
    resultaat = (math.pow(getal,4))
    if resultaat % 2 == 0:
        print(f"{resultaat} is even getal")
    else :
        print(f"{keuze} is oneven getal")

elif keuze == 3:
    x = int(input("geef een getal in"))
    y = int(input("geef een getal in"))
    z = int(input("geef een getal in"))
    if (x+y+z) < 10:
        print("klein")
    elif (x+y+z) < 100:
        print("gemiddeld")
    else :
        print("groot")
else:
    print("verkeerd")
