"""Schrijf een programma dat een willekeurig getal kiest en de gebruiker net zo lang laat gokken tot dat ze het goed hebben. """

import random

def Random():
    n = random.randint(0, 10)
    print(n)
    while True:

        gebruiker = int(input("kees een random getal tussen 0 , 10: "))
        if n == gebruiker:
            return print("je hebt gewonnen")
        else:
            print("probeer opnieuw")

Random()