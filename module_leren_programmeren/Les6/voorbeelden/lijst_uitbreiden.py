a = [5,6,8,5,7]
b = [9,58,6,528,558]

a.extend(b)
print(a)

a.append(b)
print(a)


woorden = ["paard", "ezel"]
woord1 = "kat"
woord2 = "hond"

woorden.append(woord1) # toevoegen van 1 item in totaal
print(woorden)

woorden.extend(woord2)  # extend is per letter toevoegen
print(woorden)
