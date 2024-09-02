"""
Write a program that prints the numbers from 1 to 100. But for multiples 
of three, print "Fizz" instead of the number, and for the multiples of 
five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."
"""

# decide the input
# decide for loop (if got list) while loop(not knowing where to stop)

holder= []

for numbers in range(1,99):
    if numbers%3 == 0:
        print("Fizz")
    elif  numbers %5 == 0:
        print("buzz")
    else:
        print(numbers)    

print(numbers)
