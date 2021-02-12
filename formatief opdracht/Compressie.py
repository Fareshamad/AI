"""Schrijf een compress-programma, dat uit een gegeven bestand een nieuwe bestand maakt,
 waarbij van iedere regel alle spaties en tabs aan het begin van de regel zijn verwijderd.
Verder zijn alle lege regels verwijderd (een lege regel bevat ’\n’ ,
 eventueel voorafgegaan door spaties en tabs(‘\t’))."""


bestand = open("opdracht 8.txt", "r+")
bestand_2 = open("opdracht 8 versie 2.txt", "w+")


def Compressie():

    for regel in bestand.read():
        if regel == " ":
            regel = ""
            woord = regel
        elif regel == "\n":
            regel = ""
            woord = regel
        elif regel == "\t":
            regel = ""
            woord = regel
        else:
            woord = regel
        bestand_2.writelines(woord)

Compressie()