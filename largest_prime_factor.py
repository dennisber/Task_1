prime_factor = 2
max_number = 600851475143
while prime_factor * prime_factor < max_number:
    while max_number%prime_factor == 0:
        max_number = max_number / prime_factor
    prime_factor = prime_factor + 1

print(max_number)