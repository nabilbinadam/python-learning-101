user_input = int(input("Enter the number of Adam Numbers wanted: "))

counter = 0
x = 1

while counter < user_input:
    # Square of x and reverse it
    squared_input = str(x ** 2)
    reversed_squared_input = int(''.join(reversed(squared_input)))  # Reverse the string and convert to int
    
    # Reverse x, square it and reverse the result
    reversed_x = int(str(x)[::-1])
    squared_reversed_x = reversed_x ** 2
    reversed_squared_reversed_x = int(''.join(reversed(str(squared_reversed_x))))  # Reverse the string and convert to int
    
    # Check if the reversed squared number matches the squared reversed number
    if squared_input == str(reversed_squared_reversed_x):
        print(x)
        counter += 1
    
    x += 1
