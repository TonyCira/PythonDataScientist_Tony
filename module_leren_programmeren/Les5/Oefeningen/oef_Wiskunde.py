import wiskunde as wisk

def toon_menu():
    print("1: Oppervlakte vierkant")
    print("2: Oppervlakte rechthoek")
    print("3: Oppervlakte cirkel")
    print("4: Inhoud kubus")
    print("5: Inhoud balk")
    print("6: Inhoud cilinder")
    print("stop: Programma stoppen")

toon_menu()
keuze = input("Maak je keuze: ")

while keuze != "stop":
    if keuze == "1":
        zijde = float(input("Geef de zijde: "))
        print(f"Oppervlakte: {wisk.oppv_vierkant(zijde)}")
    elif keuze == "2":
        lengte = float(input("Geef de lengte: "))
        breedte = float(input("Geef de breedte: "))
        print(f"Oppervlakte: {wisk.oppv_rechthoek(lengte, breedte)}")
    elif keuze == "3":
        straal = float(input("Geef de straal: "))
        print(f"Oppervlakte: {wisk.oppv_cirkel(straal)}")
    elif keuze == "4":
        zijde = float(input("Geef de zijde: "))
        print(f"Inhoud: {wisk.inhoud_kubus(zijde)}")
    elif keuze == "5":
        lengte = float(input("Geef de lengte: "))
        breedte = float(input("Geef de breedte: "))
        hoogte = float(input("Geef de hoogte: "))
        print(f"Inhoud: {wisk.inhoud_balk(lengte, breedte, hoogte)}")
    elif keuze == "6":
        straal = float(input("Geef de straal: "))
        hoogte = float(input("Geef de hoogte: "))
        print(f"Inhoud: {wisk.inhoud_cilinder(straal, hoogte)}")
    else:
        print("Ongeldige keuze")

    toon_menu()
    keuze = input("Maak je keuze: ")