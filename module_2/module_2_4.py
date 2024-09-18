# student: Andrey Jaroslavtsev


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in range(len(numbers)):
    if numbers[i] < 2:
        continue

    for j in range(2, int((numbers[i]//2)+1)):
        if numbers[i] % j == 0:
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
