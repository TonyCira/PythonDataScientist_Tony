dieren = ["vis","hond", "kat"]

datastring = ",".join(dieren)
print(datastring)

datastring_dieren = "paard,ezel,kameel,slang,tijger"
lijst_dieren = datastring_dieren.split()
print(*lijst_dieren)