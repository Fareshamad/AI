"""a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt."""

def count(lst, nummer):

    totaal = 0
    for x in lst:
        if x == nummer:
            totaal += 1
    print(f" nummer {nummer} komt {totaal} keren in het lijst")

# count([1,1,1,1,2,2,2,2,5,5,5,5,6,6,6,6,8,8,8],6)


"""b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt."""

def grootste_verschill(nums):
    index_lst = 0
    for i in nums:
        if index_lst > nums[i] - nums[i]:
            verschill = nums[i] - nums[i - 1]

            print(f"het grootste verschil is {verschill}")
        else:
            index_lst += 1
grootste_verschill([1,5,8,9,2,3,8,6])