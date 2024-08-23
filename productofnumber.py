def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

input_number = int(input("Insert a number: "))
result = product_of_digits(input_number)

print(f"The product of the digits of {input_number} is: {result}")