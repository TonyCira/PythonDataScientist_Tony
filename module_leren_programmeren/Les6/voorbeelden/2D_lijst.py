# 2D lijst (tabel bestaat uit rijen en kolomen)

#puntenboek wiskunde, Nederlands, Engels


jefke = [0,5,3]
inge = [9,8,9]
pieter = [7,7,7]

klas = [jefke,inge,pieter]

print(*klas)

print("Wiskunde\tNederlands\tEngels")

for leerling in klas:
    for punt in leerling:
        print("punt", end="\t\t")
    print("")

puntenboek = [
[0,5,3], # 0
[9,8,9], # 1
[7,7,7]  # 2
]

print("")
print(puntenboek[1], [1])

for index, leerling in enumerate(puntenboek):
    print(index, "|", *leerling)



