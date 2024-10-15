
n= int(input("Insert Integer:"))

while n>1:
    n=1
    if n== 1:
        print("not a valid number")

    elif n %2 == 0:
        n = n/2
        print(n)

    elif n % 2 !=0:
        n = (3*n)+ 1
        print(n)   
