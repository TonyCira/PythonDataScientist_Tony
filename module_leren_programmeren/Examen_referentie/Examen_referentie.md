# Examen-referentie: één oefening met alle functies

Dit is je **enige bron** voor het examen. Je leest één programma, begrijpt het, en past enkel aan wat de opdracht vraagt: de bestandsnaam, de kolomnummers en de tekst. Alle functies die we in de oefeningen (studenten, personeel, klasmanagement, muzikanten, docenten, cursisten) gemaakt hebben, zitten hier in één opzet.

**Zo gebruik je het op het examen**
1. Kopieer het *sjabloon* (onderdeel 2) en pas de bestandsnaam aan.
2. Kijk in de CSV welke kolom welk nummer heeft (de eerste kolom is 0).
3. Zoek in onderdeel 3 de functie die lijkt op wat de opdracht vraagt, kopieer ze en pas de kolomnummers en de tekst aan.
4. Voeg de functie toe aan het `functies`-menu en test ze.

---

## 1. De data

Het voorbeeldbestand `muzikanten.csv` heeft 6 kolommen. De kolomnummers heb je overal nodig:

| Nummer | Kolom | Type |
| --- | --- | --- |
| 0 | voornaam | tekst |
| 1 | achternaam | tekst |
| 2 | geslacht | tekst (M of V) |
| 3 | genre | tekst |
| 4 | instrument | tekst |
| 5 | uurtarief | **getal, maar in de CSV is het tekst** (gebruik `int()`) |

```csv
voornaam,achternaam,geslacht,genre,instrument,uurtarief
Lars,Vermeulen,M,Rock,Gitaar,55
Emma,Peeters,V,Pop,Zang,60
Noah,Jacobs,M,Jazz,Saxofoon,65
```

---

## 2. Het sjabloon (voor elke opgave hetzelfde)

**Vier vaste regels**
1. De lijst heet altijd `data` en de kolomnamen heten `headers`.
2. Functies hebben **geen parameters**. Ze gebruiken `headers` en `data` direct.
3. De data wordt **ingelezen vóór** de `while True`.
4. Binnen een functie heet één rij altijd `rij`. `rij[3]` is een kolom van één rij, `data[3]` is een hele rij. Schrijf nooit `data[3]` als je een kolom bedoelt.

```python
def lees_csv():
    with open(bestand, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list(reader)
    return headers, data


def update_data():
    with open(bestand, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    print("Data opgeslagen in", bestand)
```

Bovenaan het bestand:

```python
import csv
from tabulate import tabulate

bestand = "muzikanten.csv"
```

Onderaan het bestand, het hoofdprogramma:

```python
headers, data = lees_csv()

while True:
    toon_menu()
    keuze = input("\nMaak een keuze: ")

    if keuze == "0":
        update_data()
        print("Programma afgesloten.")
        break

    if keuze in functies:
        functies[keuze]()
    else:
        print("Ongeldige keuze.")
```

**Waarom dit werkt:** `functies[keuze]()` roept zonder argumenten op, dus de functies mogen geen parameters hebben. `headers` en `data` bestaan al, want ze zijn ingelezen voor de lus.

**Een controle van 10 seconden voor elke functie:** zit ik in een lus over `data`? Dan is de lusvariabele één `rij` en is elke kolom `rij[...]`.

---

## 3. De functies, per soort opdracht

### 3.1 Alles tonen

**Opdracht zegt:** "Toon alle ..." · `showindex=True` toont een nummer per rij. Dat heb je nodig bij verwijderen en aanpassen.

```python
def toon_alle():
    print(tabulate(data, headers=headers, showindex=True))
```

### 3.2 Unieke waarden van één kolom

**Opdracht zegt:** "Toon alle unieke genres / instrumenten / woonplaatsen"

Van binnen naar buiten: list comprehension haalt de kolom op, `set` verwijdert de dubbels, `sorted` zet ze in volgorde, `enumerate` geeft er een nummer bij.

**Aanpassen:** het kolomnummer (`rij[3]` wordt `rij[4]`) en de namen.

```python
def toon_genres():
    genres = sorted(set([rij[3] for rij in data]))
    for nummer, genre in enumerate(genres):
        print(nummer, genre)


def toon_instrumenten():
    instrumenten = sorted(set([rij[4] for rij in data]))
    for nummer, instrument in enumerate(instrumenten):
        print(nummer, instrument)
```

### 3.3 Filteren op een tekstwaarde

**Opdracht zegt:** "Toon iedereen met instrument x / genre x / geslacht x"

Zet de invoer **en** de kolom op `.lower()`, zodat hoofdletters geen verschil maken. Bij het geslacht gebruik je `.upper()`, want daar weet je dat het `M` of `V` is.

**Aanpassen:** kolomnummer en tekst.

```python
def toon_per_instrument():
    instrument = input("Welk instrument? ").lower()
    res = [rij for rij in data if rij[4].lower() == instrument]
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten")


def toon_per_genre():
    genre = input("Welk genre? ").lower()
    res = [rij for rij in data if rij[3].lower() == genre]
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten")


def toon_per_geslacht():
    geslacht = input("Geslacht (M/V)? ").upper()
    res = [rij for rij in data if rij[2] == geslacht]
    print(tabulate(res, headers=headers))
```

### 3.4 Filteren op een getal, met sorteren

**Opdracht zegt:** "Toon iedereen onder / boven prijs x"

**Let op:** de waarde uit de CSV is tekst, dus altijd `int(rij[5])` (eerst de kolom pakken, daarna omzetten, niet `int(rij)[5]`). Sorteren op een getal doe je met `key=lambda rij: int(rij[5])`. `reverse=True` is aflopend. Is het kommagetal, gebruik dan `float()`.

**Aanpassen:** `<` of `>`, het kolomnummer en `int` of `float`.

```python
def toon_onder_prijs():
    prijs = int(input("Maximaal uurtarief: "))
    res = [rij for rij in data if int(rij[5]) < prijs]
    res = sorted(res, key=lambda rij: int(rij[5]))
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten onder de {prijs} euro per uur")


def toon_boven_prijs():
    prijs = int(input("Minimaal uurtarief: "))
    res = [rij for rij in data if int(rij[5]) > prijs]
    res = sorted(res, key=lambda rij: int(rij[5]), reverse=True)
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten boven de {prijs} euro per uur")
```

### 3.5 Zoeken op een deel van een tekst

**Opdracht zegt:** "Zoek op naam"

`zoek in rij[1].lower()` controleert of een stukje tekst in de achternaam zit.

```python
def zoek_op_achternaam():
    zoek = input("Zoek op (een deel van) de achternaam: ").lower()
    res = [rij for rij in data if zoek in rij[1].lower()]
    print(tabulate(res, headers=headers))
```

### 3.6 Sorteren

**Opdracht zegt:** "Sorteer op uurtarief aflopend (9-0)"

`sorted()` maakt een nieuwe lijst en laat `data` ongemoeid. Gebruik nooit `x = data.sort()`: dat geeft `None`. Oplopend: haal `reverse=True` weg.

```python
def toon_sorteer_op_tarief():
    res = sorted(data, key=lambda rij: int(rij[5]), reverse=True)
    print(tabulate(res, headers=headers))
```

### 3.7 Tellen met een dictionary

**Opdracht zegt:** "Toon het aantal ... per ..."

`aantal.get(genre, 0)` geeft het huidige aantal, of 0 als het genre er nog niet in zit. Daar tel je 1 bij.

```python
def toon_aantal_per_genre():
    aantal = {}
    for rij in data:
        genre = rij[3]
        aantal[genre] = aantal.get(genre, 0) + 1
    for genre, n in sorted(aantal.items()):
        print(f"{genre}: {n}")
```

### 3.8 Sets: wie wel A maar niet B

**Opdracht zegt:** "Toon wie ... volgt/speelt maar niet ..." of "wie beide"

Maak voor elke groep een set met namen en reken met de sets: `a - b` (verschil), `a & b` (doorsnede, beide), `a | b` (unie, minstens één), `a ^ b` (precies één).

```python
def toon_genre_niet_instrument():
    genre = input("Welk genre spelen ze? ").lower()
    instrument = input("Welk instrument spelen ze niet? ").lower()
    in_genre = set([rij[0] + " " + rij[1] for rij in data if rij[3].lower() == genre])
    met_instrument = set([rij[0] + " " + rij[1] for rij in data if rij[4].lower() == instrument])
    for naam in sorted(in_genre - met_instrument):
        print(naam)
```

### 3.9 Laagste, hoogste en gemiddelde, met een tuple

**Opdracht zegt:** "Toon het laagste/hoogste/gemiddelde ..."

`return min(...), max(...)` geeft **een tuple** terug. Je pakt ze uit met `laagste, hoogste = bereken_min_max()`. Het gemiddelde is `sum / len`, met `round(..., 2)` voor twee decimalen.

```python
def bereken_min_max():
    tarieven = [int(rij[5]) for rij in data]
    return min(tarieven), max(tarieven)


def toon_statistiek():
    tarieven = [int(rij[5]) for rij in data]
    laagste, hoogste = bereken_min_max()
    gemiddelde = round(sum(tarieven) / len(tarieven), 2)
    print(f"Laagste tarief: {laagste}")
    print(f"Hoogste tarief: {hoogste}")
    print(f"Gemiddeld tarief: {gemiddelde}")
```

### 3.10 Toevoegen

**Opdracht zegt:** "Voeg een ... toe"

Vraag elk veld, maak de tekst netjes (`capitalize`, `title`, `upper`), zet getallen om met `int()` en voeg een rij toe met `data.append([...])`. De volgorde moet gelijk zijn aan de kolommen van de CSV.

```python
def voeg_toe():
    voornaam = input("Voornaam: ").capitalize()
    achternaam = input("Achternaam: ").title()
    geslacht = input("Geslacht (M/V): ").upper()
    genre = input("Genre: ").capitalize()
    instrument = input("Instrument: ").capitalize()
    uurtarief = int(input("Uurtarief: "))
    data.append([voornaam, achternaam, geslacht, genre, instrument, uurtarief])
    print("Muzikant toegevoegd")
```

### 3.11 Verwijderen

**Opdracht zegt:** "Verwijder een ..."

Toon eerst met nummers, vraag het nummer, controleer `0 <= nummer < len(data)` (anders `IndexError`) en gebruik `data.pop(nummer)`.

```python
def verwijder():
    toon_alle()
    nummer = int(input("Nummer van de muzikant: "))
    if 0 <= nummer < len(data):
        data.pop(nummer)
        print("Muzikant verwijderd")
    else:
        print("Ongeldig nummer")
```

### 3.12 Aanpassen

**Opdracht zegt:** "Pas ... aan" (met een keuze) of "Pas het tarief aan"

Zelfde opbouw als verwijderen. Bij een keuze (instrument of genre) gebruik je `if / elif / else`. Aanpassen doe je met `data[nummer][kolom] = nieuwe_waarde`.

```python
def pas_genre_of_instrument_aan():
    toon_alle()
    nummer = int(input("Nummer van de muzikant: "))
    if 0 <= nummer < len(data):
        keuze = input("Wil je het instrument of het genre aanpassen? ").lower()
        if keuze == "instrument":
            data[nummer][4] = input("Nieuw instrument: ").capitalize()
        elif keuze == "genre":
            data[nummer][3] = input("Nieuw genre: ").capitalize()
        else:
            print("Kies instrument of genre")
    else:
        print("Ongeldig nummer")


def pas_tarief_aan():
    toon_alle()
    nummer = int(input("Nummer van de muzikant: "))
    if 0 <= nummer < len(data):
        data[nummer][5] = int(input("Nieuw uurtarief: "))
        print("Tarief aangepast")
    else:
        print("Ongeldig nummer")
```

### 3.13 Wegschrijven

**Opdracht zegt:** "Update data / schrijf weg naar de CSV"

Dit is `update_data()` uit onderdeel 2: modus `"w"`, eerst `writerow(headers)` voor één rij en dan `writerows(data)` voor alle rijen. Niet `"r"` en niet `writerow(data)`.

---

## 4. Het menu

```python
def toon_menu():
    print("\n" + "=" * 40)
    print("      MUZIKANTEN")
    print("=" * 40)
    print("1  - Toon alle muzikanten")
    print("2  - Toon alle unieke genres")
    print("3  - Toon alle unieke instrumenten")
    print("4  - Toon muzikanten met instrument x")
    print("5  - Toon muzikanten met genre x")
    print("6  - Toon jongens of meisjes")
    print("7  - Toon muzikanten onder vraagprijs x")
    print("8  - Toon muzikanten boven vraagprijs x")
    print("9  - Zoek op achternaam")
    print("10 - Sorteer op uurtarief (aflopend)")
    print("11 - Toon aantal muzikanten per genre")
    print("12 - Toon genre x maar niet instrument y")
    print("13 - Toon laagste, hoogste en gemiddeld tarief")
    print("14 - Voeg muzikant toe")
    print("15 - Verwijder muzikant")
    print("16 - Pas genre of instrument aan")
    print("17 - Pas uurtarief aan")
    print("18 - Update data (opslaan)")
    print("0  - Stoppen (slaat ook op)")
```

```python
functies = {
    "1": toon_alle,
    "2": toon_genres,
    # ...
    "18": update_data,
}
```

Na een nieuwe functie: één regel in `functies` (zonder haakjes) en één `print` in `toon_menu`.

---

## 5. Addertjes: dingen die op het examen kunnen verrassen

**Meerdere waarden in één cel** (bijvoorbeeld `Python;SQL`). Splits eerst, dan pas vergelijken:

```python
res = [rij for rij in data if "sql" in rij[2].lower().split(";")]
```

Bij toevoegen zet je de waarden weer samen met `";".join(lijst)`.

**Hoofdletters.** `"sql".title()` geeft `"Sql"` en past dus niet bij `"SQL"` in het bestand. Zet bij het zoeken beide kanten op `.lower()`.

**Getallen in de CSV zijn tekst.** Alfabetisch komt `"10.0"` voor `"7.0"`. Sorteer en vergelijk daarom altijd met `int()` of `float()`.

**Een lege cel.** `"".split(";")` geeft `['']` en dus geen lege lijst. Controleer dat als een cel leeg kan zijn.

**Meerdere CSV's** (een per campus): gebruik een dictionary met de naam als key en een lus.

```python
campussen = {}
for campus in ["genk", "pelt"]:
    headers, campussen[campus] = lees_campus(campus)
```

Een rij verplaatsen is `pop` uit de ene lijst en `append` aan de andere.

---

## 6. Controlelijst voor je op Run drukt

- Staat `import csv` en `from tabulate import tabulate` bovenaan?
- Lees ik de data in vóór de `while True`?
- Hebben mijn functies geen parameters, en staat in `functies` geen `()` achter de naam?
- Gebruik ik `rij[...]` voor een kolom en `data[...]` alleen voor een hele rij?
- Zet ik getallen uit de CSV om met `int()` of `float()`?
- Schrijf ik weg met `"w"`, `writerow(headers)` en `writerows(data)`?
- Heb ik gecontroleerd dat het nummer in `0 <= nummer < len(data)` zit?
- Heb ik na het wegschrijven het CSV-bestand geopend om te kijken of het klopt?

---

## 7. Het volledige programma

Dit is `referentie_programma.py`: alles samen, getest met `muzikanten.csv`.

```python
import csv
from tabulate import tabulate

bestand = "muzikanten.csv"


# =====================
# INLEZEN EN WEGSCHRIJVEN
# =====================

def lees_csv():
    with open(bestand, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list(reader)
    return headers, data


def update_data():
    with open(bestand, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    print("Data opgeslagen in", bestand)


# =====================
# TONEN
# =====================

def toon_alle():
    print(tabulate(data, headers=headers, showindex=True))


def toon_genres():
    genres = sorted(set([rij[3] for rij in data]))
    for nummer, genre in enumerate(genres):
        print(nummer, genre)


def toon_instrumenten():
    instrumenten = sorted(set([rij[4] for rij in data]))
    for nummer, instrument in enumerate(instrumenten):
        print(nummer, instrument)


def toon_per_instrument():
    instrument = input("Welk instrument? ").lower()
    res = [rij for rij in data if rij[4].lower() == instrument]
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten")


def toon_per_genre():
    genre = input("Welk genre? ").lower()
    res = [rij for rij in data if rij[3].lower() == genre]
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten")


def toon_per_geslacht():
    geslacht = input("Geslacht (M/V)? ").upper()
    res = [rij for rij in data if rij[2] == geslacht]
    print(tabulate(res, headers=headers))


def toon_onder_prijs():
    prijs = int(input("Maximaal uurtarief: "))
    res = [rij for rij in data if int(rij[5]) < prijs]
    res = sorted(res, key=lambda rij: int(rij[5]))
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten onder de {prijs} euro per uur")


def toon_boven_prijs():
    prijs = int(input("Minimaal uurtarief: "))
    res = [rij for rij in data if int(rij[5]) > prijs]
    res = sorted(res, key=lambda rij: int(rij[5]), reverse=True)
    print(tabulate(res, headers=headers))
    print(f"{len(res)} muzikanten boven de {prijs} euro per uur")


def zoek_op_achternaam():
    zoek = input("Zoek op (een deel van) de achternaam: ").lower()
    res = [rij for rij in data if zoek in rij[1].lower()]
    print(tabulate(res, headers=headers))


def toon_sorteer_op_tarief():
    res = sorted(data, key=lambda rij: int(rij[5]), reverse=True)
    print(tabulate(res, headers=headers))


# =====================
# TELLEN, SETS EN TUPLE
# =====================

def toon_aantal_per_genre():
    aantal = {}
    for rij in data:
        genre = rij[3]
        aantal[genre] = aantal.get(genre, 0) + 1
    for genre, n in sorted(aantal.items()):
        print(f"{genre}: {n}")


def toon_genre_niet_instrument():
    genre = input("Welk genre spelen ze? ").lower()
    instrument = input("Welk instrument spelen ze niet? ").lower()
    in_genre = set([rij[0] + " " + rij[1] for rij in data if rij[3].lower() == genre])
    met_instrument = set([rij[0] + " " + rij[1] for rij in data if rij[4].lower() == instrument])
    for naam in sorted(in_genre - met_instrument):
        print(naam)


def bereken_min_max():
    tarieven = [int(rij[5]) for rij in data]
    return min(tarieven), max(tarieven)


def toon_statistiek():
    tarieven = [int(rij[5]) for rij in data]
    laagste, hoogste = bereken_min_max()
    gemiddelde = round(sum(tarieven) / len(tarieven), 2)
    print(f"Laagste tarief: {laagste}")
    print(f"Hoogste tarief: {hoogste}")
    print(f"Gemiddeld tarief: {gemiddelde}")


# =====================
# TOEVOEGEN, AANPASSEN, VERWIJDEREN
# =====================

def voeg_toe():
    voornaam = input("Voornaam: ").capitalize()
    achternaam = input("Achternaam: ").title()
    geslacht = input("Geslacht (M/V): ").upper()
    genre = input("Genre: ").capitalize()
    instrument = input("Instrument: ").capitalize()
    uurtarief = int(input("Uurtarief: "))
    data.append([voornaam, achternaam, geslacht, genre, instrument, uurtarief])
    print("Muzikant toegevoegd")


def verwijder():
    toon_alle()
    nummer = int(input("Nummer van de muzikant: "))
    if 0 <= nummer < len(data):
        data.pop(nummer)
        print("Muzikant verwijderd")
    else:
        print("Ongeldig nummer")


def pas_genre_of_instrument_aan():
    toon_alle()
    nummer = int(input("Nummer van de muzikant: "))
    if 0 <= nummer < len(data):
        keuze = input("Wil je het instrument of het genre aanpassen? ").lower()
        if keuze == "instrument":
            data[nummer][4] = input("Nieuw instrument: ").capitalize()
        elif keuze == "genre":
            data[nummer][3] = input("Nieuw genre: ").capitalize()
        else:
            print("Kies instrument of genre")
    else:
        print("Ongeldig nummer")


def pas_tarief_aan():
    toon_alle()
    nummer = int(input("Nummer van de muzikant: "))
    if 0 <= nummer < len(data):
        data[nummer][5] = int(input("Nieuw uurtarief: "))
        print("Tarief aangepast")
    else:
        print("Ongeldig nummer")


# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle,
    "2": toon_genres,
    "3": toon_instrumenten,
    "4": toon_per_instrument,
    "5": toon_per_genre,
    "6": toon_per_geslacht,
    "7": toon_onder_prijs,
    "8": toon_boven_prijs,
    "9": zoek_op_achternaam,
    "10": toon_sorteer_op_tarief,
    "11": toon_aantal_per_genre,
    "12": toon_genre_niet_instrument,
    "13": toon_statistiek,
    "14": voeg_toe,
    "15": verwijder,
    "16": pas_genre_of_instrument_aan,
    "17": pas_tarief_aan,
    "18": update_data,
}


def toon_menu():
    print("\n" + "=" * 40)
    print("      MUZIKANTEN")
    print("=" * 40)
    print("1  - Toon alle muzikanten")
    print("2  - Toon alle unieke genres")
    print("3  - Toon alle unieke instrumenten")
    print("4  - Toon muzikanten met instrument x")
    print("5  - Toon muzikanten met genre x")
    print("6  - Toon jongens of meisjes")
    print("7  - Toon muzikanten onder vraagprijs x")
    print("8  - Toon muzikanten boven vraagprijs x")
    print("9  - Zoek op achternaam")
    print("10 - Sorteer op uurtarief (aflopend)")
    print("11 - Toon aantal muzikanten per genre")
    print("12 - Toon genre x maar niet instrument y")
    print("13 - Toon laagste, hoogste en gemiddeld tarief")
    print("14 - Voeg muzikant toe")
    print("15 - Verwijder muzikant")
    print("16 - Pas genre of instrument aan")
    print("17 - Pas uurtarief aan")
    print("18 - Update data (opslaan)")
    print("0  - Stoppen (slaat ook op)")


# =====================
# HOOFDPROGRAMMA
# =====================

headers, data = lees_csv()

while True:
    toon_menu()
    keuze = input("\nMaak een keuze: ")

    if keuze == "0":
        update_data()
        print("Programma afgesloten.")
        break

    if keuze in functies:
        functies[keuze]()
    else:
        print("Ongeldige keuze.")
```
