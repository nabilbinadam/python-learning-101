"""Validate Credit Card Number
Get a credit card number as input. Create a function that validates the credit card number 
based on the Luhn algorithm.

The function must return True if the credit card number is valid.
If the function returns True, print "Credit Card Number is valid."
Valid credit card number
4539 3195 0343 6467

The first step of the Luhn algorithm is to double every second digit, starting from the right. F
or example: 4_3_ 3_9_ 0_4_ 6_6_
If doubling the number results in a value greater than 9, subtract 9 from the product. 
The results of doubling are: 8569 6195 0383 3437
Next, sum all the digits: 8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80
If the sum is divisible by 10, then the credit card number is valid. Therefore, this number is valid!"""

user_input=str(input("insert credit card:"))


def doubling(user_input):
      
    counter =[]
    for i in range(len(user_input)- 1, -1, -2):
      #print(user_input[i])
      ranging = int(user_input[i])*2
      counter.append(ranging)
      print(counter)
      
    
    
    return counter    


result = doubling(user_input) 
#check=checkDoublingGreaterThan9()
def checkDoublingGreaterThan9(result):
    sub=[]
    for i in result :
     if i < 9 :
       subtract = i - 9
       sub.append(subtract)
       print (sub)
    return sub









"""

doubling(user_input)
checkDoublingGreaterThan9(counter)  

def sumDigit(result):
   additional = 
   return additional

def Divisible(additional):
   if additional % 10 ==0 :
      print("Credit Card is Valid ") 

"""