
for input in range(2, 100):
    is_prime = True  # Assume the number is prime
    
    # Check divisibility from 2 up to the integer square root of the input
    for divisor in range(2, int(input**0.5) + 1):
        if input % divisor == 0:
            is_prime = False
            break  # No need to check further if divisible

    # If the number is still assumed to be prime, print it
    if is_prime:
        print(input)











