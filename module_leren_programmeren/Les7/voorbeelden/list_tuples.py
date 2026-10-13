# tuple met 3 lijsten

secret_number = ([7,12,23,33,41,57],[7,8,6,55,44])
secret_number[0].append(9) # inhoud van de lijsten kan veranderen
                        # maar binnen de tuple kan ik geen lijst toevoegen



for row in secret_number:
    print(row)

secret_number = [([7,12,23,33,41,57],[7,8,6,55,44]),[7,4,2,3] ]

for list_item in secret_number:
    print(list_item)