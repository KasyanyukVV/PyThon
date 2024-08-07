numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for number in numbers:
    if number == 1:
        continue
    if is_prime(number):
        primes.append(number)
    else:
        not_primes.append(number)
print(primes)
print(not_primes)
