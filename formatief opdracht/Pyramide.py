" Pyramide, for loop"


def Pyramide():
    lengte  = int(input("geeft de lengte van de Pyramide: "))

    for i in range(lengte):
        for j in range((lengte - i) - 1):
            print(end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
Pyramide()