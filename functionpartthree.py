#recursivefunction
'''
user_input=int(input("Insert Decimal"))
factorial = 1 
def  factorial(user_input):
    
    for x in range(user_input,0,-1) :
        
        factorial = factorial * x 
        
        print("factorial of",user_input,"is",factorial)
        
        
factorial()        
'''

#define based case

def sumofdigits(n):
    #base case
    if n==0 :
     return 0
    else:
        return (n %10) + sumofdigits(n//10)
    
    
print(sumofdigits(97409))    


    