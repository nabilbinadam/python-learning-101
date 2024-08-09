# Define the input number
user_input = 13

# Calculate the square of the input number
squared_check = user_input ** 2

# Reverse the digits of the input number
counter = 0
number = user_input
while number > 0:
    counter = counter * 10 + number % 10
    number //= 10

inputTwo = counter

# Calculate the square of the reversed number
inputTwoSquared = inputTwo ** 2

# Reverse the digits of the squared value of the original number
reverse_check = 0
temp = squared_check
while temp > 0:
    reverse_check = reverse_check * 10 + temp % 10
    temp //= 10

# Reverse the digits of the squared value of the reversed number
counterTwo = 0
temp = inputTwoSquared
while temp > 0:
    counterTwo = counterTwo * 10 + temp % 10
    temp //= 10

# Check if the reversed square of the input number matches the square of the reversed input number
if reverse_check == counterTwo:
    print(f"{user_input} is an Adam Number")
else:
    print(f"{user_input} is not an Adam Number")
