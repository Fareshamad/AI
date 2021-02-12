def Fibonaci(n):
   if n <= 1:
       return 1
   else:
       return(Fibonaci(n-1) + Fibonaci(n-2))

while True:
    fn = int(input("hoeveel aantal getalen wil je hebben? "))
    if fn <= 0:
       print("je moet een posetive getal invullen ")
    else:
        for i in range(fn):
           print(Fibonaci(i))
        break
Fibonaci(fn)