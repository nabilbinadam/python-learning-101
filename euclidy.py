
a = int(input("a:"))
b = int(input("b:"))


while b!=0 :

    Remainder = a%b
    a = b
    b= Remainder
    
   

print("GCD is:", a)   