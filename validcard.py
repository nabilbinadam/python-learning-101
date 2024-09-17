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


input = [int(input("Insert Credit Card :"))]

def doubling(input):
    for i in range(len(input)-1,len(input),-2) :
       multi = input[i] * 2
       return multi





print(doubling(input))  