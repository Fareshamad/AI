def Tekstcheck():
    str1 = str(input("geef je eerste zin:"))
    str2 = str(input("geef je tweede zin:"))

    begin = 0

    for x in str1:
        if x != str2:
            verschill = str1.index(x)
            return print(f"het verschill is {verschill}")
        else:
            begin += 1
Tekstcheck()
