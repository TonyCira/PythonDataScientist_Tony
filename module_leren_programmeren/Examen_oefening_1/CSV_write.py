import csv

data = [
     ["naam","klas","woonplaats"],
     ["Anke","1a","As"],
     ["Ben","1a","Genk"],
     ["Fien","2a","Genk"],
     ["Cindy","2b","Hasselt"]
]

with open("studenten.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

