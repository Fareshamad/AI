"""Schrijf een functie die het gemiddelde van een lijst met cijfers berekent.
 Schrijf er ook een die als input een lijst van lijsten met cijfers krijgt, en als uitvoer een lijst met de gemiddelden teruggeeft."""

def gemiddeld(num):
    return sum(num) / len(num)

print(gemiddeld([5,6,9,8,7,9,6,2,5,4]))

"""gemiddeld berkenen met input"""

aantaal_elementen = int(input("voer het aantaal elementen  in : "))
nummers = list(map(int, input("voer de nummers in met een spaties er tussen : ").strip().split()))[:aantaal_elementen]

print(gemiddeld(nummers))

