'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

num = 600851475143
end = int(sqrt(num))

def is_prime(n):
    if any(n % i == 0 for i in range(2, n)) == True:    # Using any because it breaks operation as soon as any True is found.
        return False
    else:
        return True

primes = []

if num % 2 == 0:            # Treat 2 seperately as it is the only even prime number
    primes.append(2)

for i in range(3, end, 2):  # Only check odd numbers increases speed by 2
    if num % i == 0 and is_prime(i):
        primes.append(i)

print(max(primes))