binair_getal = "100011001"
decimaal_getal = int(binair_getal,2)
print(decimaal_getal)

# string convert naar een int

binair_getal = bin(decimaal_getal)
print(type(binair_getal))
print(binair_getal)  # ob geeft aan dat het een binair getal is

for teken in binair_getal:
    print(teken)

print(binair_getal[2:]) # getal zonder 0b






