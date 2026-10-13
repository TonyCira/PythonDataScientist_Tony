beschermde_data = ("Admin", "1234", "ABCD")
niet_beschermde_data = ["Admin", "1234", "ABCD"]

# key difference vierkante haakjes read en aanpasbaar = list
# in tuple met haakjes is het een read only en kan niet aangepast worden

print(type(beschermde_data))
print(beschermde_data[0])

for data in beschermde_data:
    print(data)

print(*niet_beschermde_data)




#hoe verander ik data in een tuple.

beschermde_data = list(beschermde_data)
beschermde_data.append("Dit zou niet mogen")
beschermde_data = tuple(beschermde_data)
print(beschermde_data)

