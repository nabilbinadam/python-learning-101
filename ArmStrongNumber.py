user_input = int(input("Enter the number of Armstrong Numbers wanted: "))

count = 0
num = 1

while count < user_input:
    # Convert num to string to process each digit
    str_num = str(num)
    num_digits = len(str_num)
    
    # Calculate the sum of digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_num)
    
    # Check if num is an Armstrong number
    if armstrong_sum == num:
        print(num)
        count += 1
    
    num += 1
