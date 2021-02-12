"""dat is mijn sorteer functie uit Blok B :) """

def my_sort(lst):

    lst_sorted = lst.copy()
    for i in range(len(lst_sorted)):
        sorteer = True
        for getal in range(0, len(lst_sorted) - 1):
            if lst_sorted[getal] > lst_sorted[getal + 1]:
                lst_sorted[getal], lst_sorted[getal + 1] = lst_sorted[getal + 1], lst_sorted[getal]
                sorteer = False
        if sorteer:
            break
    return lst_sorted

print(my_sort([5,8,9,3,5,7,8,8,5,2,4]))
