

def add(number1,number2):
    
    
    return number1 + number2
    
    
    

print(add(1,2)) 


#function is purely for organizing our code

def greeting(name) : 
    
    print( "good Morning", str(name))


user_name = str(input("insert name"))
greeting(user_name)

def simple_interest (principle,period,rate):
    interest = ( principle * period * rate) /100
    return interest
    
    
simple_interest(500,300,200)    