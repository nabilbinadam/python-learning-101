def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def twin_primes(limit):
    twin_prime_pairs = []
    prev_prime = 0  

    for num in range(3, limit, 2):  
        if is_prime(num):
            if prev_prime and (num - prev_prime == 2):
                twin_prime_pairs.append((prev_prime, num))
            prev_prime = num  

    return twin_prime_pairs


result = twin_primes(1000)
for pair in result:
    print(pair)