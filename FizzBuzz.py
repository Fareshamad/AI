"""Schrijf een programma dat de getallen 1 tot 100 print, maar print voor veelvouden van drie “fizz” in plaats van het getal en voor veelvouden van vijf print “buzz” in plaats van
het getal. Getallen die zowel veelvoud zijn van drie als van vijf worden afgedrukt als “fizzbuzz”"""


def FizzBuzz():
    for fizzbuzz in range(0,101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)
print(FizzBuzz())