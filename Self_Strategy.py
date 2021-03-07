"" "MASTER MIND" ""
import random
from itertools import product

kleuren = ["R", "G", "B", "Z", "P", "O"]
combinatie = []
visited = []
vlag = [1, 1, 1, 1]

def begin():
    """Hier wordt de begin menu getoont waar bij de gebruiker kiest tussen de regels van het spel of het starten van
    het spel of het stoppen van het spel. """

    print("                                                    **************************************")
    print("                                                     WELKOM BIJ MATSER MIND ARE YOU READY?")
    print("                                                    **************************************\n")
    print("                                                          ========================")
    print("                                                          || 1.uitleg en regels ||")
    print("                                                          || 2.start het spel   || ")
    print("                                                          || 3.stoppen          ||")
    print("                                                          ========================\n")
    keuze = input("                                                      voer uw keuze in {1}, {2} of {3}: ")
    print("                                                 -------------------------------------------\n")


    while True:

        if keuze == "1":
            print("\ndat is fijn, hier zijn alle regels voor het spelletje: ")
            print("----------------------------------------------------------")
            regels()
            break
        elif keuze == "2":
            print("\nwat goed dat u het spelletje wil spellen,\nik hoop dat uu klaar voor bent :)")
            print("-------------------------------------------------------------------------------")
            tegenstander()
            break
        elif keuze == "3":
            print("bedankt voor het spelen :-) ")
            break
        else:
            print("FOUT probeer opnieuw: \n")
            print("========================")
            print("|| 1.uitleg en regels ||\n|| 2.start het spel   ||\n|| 3.stoppen          ||")
            print("========================")
            keuze = input("voer uw keuze in {1}, {2} of {3}: ")
            print("-------------------------------------------\n")


def regels():
    """"een functie waar bij alle game regels worden getoont """

    print(
        "\nUITLEG:\nBij Master Mind draait het allemaal om logisch nadenken, de juiste keuzes maken en concentratie.\n"
        "Het doel van het spel is om de kleurcode van de computer te achterhalen.\n"
        "De computer  is de codemaker, deze dient een code te maken met vier gekleurde pionnen.\n"
        "Deze code is alleen zichtbaar voor de computer, er kan gekozen worden uit vijf verschillende kleuren.\n")
    print(
        "REGELS:\n1. De computer zal en code maken van vier kleuren.\n2. De speler krijg 8 pogingen om de code te "
        "kraken. "
        "\n3. De speler krijgt bij elke poging een feedback."
        "\n4. Feedback bestaat uit twee pinnen {Zwart} en {Wit}."
        "\n5. Als de speler Zwart pin krijg dan heeft ie een juiste kleuer op de juiste plek."
        "\n6. Als de speler Wit pin krijg dan heeft hij een juiste kleur maar niet op de juiste plek."
        "\n7. ALs de gebruiker helemaal niks krijgt dan heeft hij helemaal niks goed.\n")
    terug = (input("Ik hoop dat u met veel plezier het spelletje speelt, succes\n"
                   "druk op {1} om het begin menu te kunnen zien : "))
    while True:
        if terug == "1":
            begin()
            break
        else:
            print("\nFOUT, u moet 1 kiezen om de begin menu te kunnen zien.\n")
            terug = (input("druk op {1} om het begin menu te kunnen zien : "))

def tegenstander():
    """een functie waar bij u tegenstander mag kiezen.


    als de gebruiker op 1 drukt dan wordt de code voor hem gemaakt en hij mag het krakken.

    en als de gebruiker op 2 drukt dan moet hij zelf de code maken voor de computer om te krakken.
        """

    print("Alright here we go, u mag kiezen uit de volgende opties: \n"
          "\n1. De computer tegen u."
          "\n2. u tegen de computer. ")
    keuze = input("Hier mag u keuze invullen 1 of 2? ")
    if keuze == "1":
        print("\nTop! dan gaat de computer een geheim code maken. ")
        start_spel_computer()
    elif keuze == "2":
        print("Top! u mag dan zo meteen de code maken voor de computer. \n")
        start_spel_gebruiker()
    else:
        begin()


def start_spel_computer():
    """Hier maakt de computer voor de gebruiker om te kunnen krakken een vervolgens wordt een feedback op gegeven met
    zwart en wit pinnen """


    pogingen = 8

    print(
        "de letters staan voor de hoofdletter van de kleuren.\nDus 'R' voor Rood en 'G' voor Groen en 'B' voor blauw "
        "en 'Z' voor Zwart en 'P' voor Paars en 'O' voor Oranje.")
    kleuren = ["R", "G", "B", "Z", "P", "O"]
    print(kleuren)
    code = random.sample(kleuren, 4)  # een random sample maken
    print(code)

    while True:
        print(f"u hebt {pogingen} pogingen: ")
        gok = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
            "kies derde kleuren : ").upper(), input("kies vierde kleuren: ").upper()

        while True:
            if any(x in kleuren for x in gok):
                break
            else:
                print("\nDat is een ongeldig invoer, probeer opnieuw! ")
                print(f"hier zijn alle kleuren opnieuw {kleuren}")

                gok = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
                    "kies derde kleuren : ").upper(), input("kies vierde kleuren: ").upper()

        zwart_pin, wit_pin = feedback(gok, code)
        if zwart_pin == 4:
            print("Gefeliciteerd je hebt gewonnen !!")
            break

        print(f"zwarte pin: {zwart_pin}\nwit pin: {wit_pin}\ngok: {gok}")
        pogingen -= 1

        if pogingen < 1:
            print("Helaas je kan de code niet krakken! ")
            break


def start_spel_gebruiker():
    """Hier maakt de gebruiker de code voor de computer om te kunnen krakken een vervolgens wordt een feedback op
    gegeven met zwart en wit pinnen """


    print(
        "de letters staan voor de hoofdletter van de kleuren.\nDus 'R' voor Rood en 'G' voor Groen en 'B' voor blauw "
        "en 'Z' voor Zwart en 'P' voor Paars en 'O' voor Oranje.")
    kleuren = ["R", "G", "B", "Z", "P", "O"]
    print(f"hier zijn alle kleuren {kleuren} ")
    print("\nu mag een code maken voor de computer van 4 kleuren: ")

    code = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
        "kies derde kleuren : ").upper(), input("kies vierde kleuren: ").upper()
    while True:
        if any(x in kleuren for x in code):
            print(f"dat is uw code {code} \n")
            break
        else:
            print("\nDat is een ongeldig invoer, probeer opnieuw! ")
            print(f"hier zijn alle kleuren opnieuw {kleuren}")

            code = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
                "kies derde kleuren:  ").upper(), input("kies vierde kleuren: ").upper()
    pogingen = 1300
    maak_gok = []
    zwart_pin, wit_pin = 0, 0
    while True:
        if pogingen == 1300:
            maak_gok = oplossing_self(0, 0)
            zwart_pin, wit_pin = feedback(maak_gok, code)
            print(f"zwarte pinnen: {zwart_pin}, witte pinnen: {wit_pin}, and gokken: {maak_gok}")
        else:
            if pogingen < 1:
                print("Helaas je kan de code niet krakken.")
                break

            maak_gok = oplossing_self([zwart_pin, wit_pin], maak_gok)
            zwart_pin, wit_pin = feedback(maak_gok, code)
            print(f"zwarte pinnen: {zwart_pin}, witte pinnen: {wit_pin}, and gokken: {maak_gok}")

        if zwart_pin == 4:
            print('Gefeliciteerd je hebt gewonnen!!! ')
            break
        pogingen -= 1


def oplossing_self(antwoord, huidge_gok):

    """ dat is een algortime die ik zelf heb bedacht hij begint altijd met de gok "z,z,z,z" en als hij geen feedback
    krijgt dan maakt hij een nieuwe gok met vier kleuren die het zelfde zijn.
    wanneer er feedback is met een zwart pin dan verander hij de laatste index met een nieuwe kleur tot dat ie alle kleuren
    door loopt en daarna doet ie het zelfde met [-1] tot dat ie het code kraakt.
"""

    volgende_gok = []

    if antwoord == 0:
        kleuren = ['R', 'G', 'B', 'O', 'P', 'Z']
        for i in product(kleuren, repeat=4):
            combinatie.append(list(i))
        volgende_gok = combinatie[-1]
        visited.append(volgende_gok)
    else:
        for x in combinatie:
            if x in visited:
                continue
            else:
                if 0 not in vlag:
                    volgende_gok = x
                    visited.append(volgende_gok)
                    break
                else:
                    juiste_index = []
                    for i in range(4):
                        if vlag[i] == 0:
                            juiste_index.append(i)

                    matched = 0
                    for index in juiste_index:
                        if x[index] == huidge_gok[index]:
                            matched += 1
                        else:
                            continue
                    if matched == len(juiste_index):
                        volgende_gok = x
                        visited.append(volgende_gok)
                        break
                    else:
                        continue

    return volgende_gok


def feedback(gok ,code):

    """deze functie laat de feedback zien op de gok die de computer of de gebruiker maakt."""


    code1 = list(code)
    zwart_pin = 0
    wit_pin = 0
    oude_gok = []
    # hier loop ik door de lengte van de gok
    for x in range(len(gok)):
        #hier check ik als de gok[x] gelijk aan de code[x] dan heeft hij een zwart pin
        if gok[x] == code1[x]:
            zwart_pin += 1
            oude_gok.append(x)

    copy = code1[::]
    for x in oude_gok:
        copy.remove(code1[x])
    for i in range(4):
        if i not in oude_gok:
            if gok[i] in copy:
                wit_pin += 1
                copy.remove(gok[i])

    return zwart_pin, wit_pin


    # zwart_pin = 0
    # wit_pin = 0
    #
    # for i in range(4):
    #     if gok[i] == code[i]:
    #         vlag[i] = 0
    #         zwart_pin += 1
    #
    # for i in range(4):
    #     if vlag[i] == 1 and gok[i] in code[i]:
    #         wit_pin += 1
    # return zwart_pin, wit_pin





begin()
