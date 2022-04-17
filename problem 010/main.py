
import sys
sys.path.append("C://Users//jrpyles//Desktop//projectEuler//libraries")
from myLibrary import prime_check

import time
tic = time.perf_counter()

def coprime_check(basis, x):
    for i in basis:
        if x%i == 0:
            return False
    return True

# d is the number not to be exceeded. p is the size of our basis of wheel factorization. Larger numbers should reduce computational complexity.

d = 110000
basis_size = 3

#Generates basis
basis = []
x = 1
while len(basis) < basis_size:
    x += 1
    if prime_check(x) == True:
        basis.append(x)

#Generate "x", the product of all basis values
x = 1
for i in basis:
    x *= i

#Generate primes under 2x
prime_sum = 0
for i in range(2, 2*x):
    if prime_check(i):
        prime_sum += i

#Generate columns
columns = []
for i in range(x, 2*x):
    if coprime_check(basis, i):
        columns.append(i - x)

n = x
g = 2
while n < d:
    for i in columns:
        n = g*x + i
        if n > d:
            continue
        if prime_check(n):
            prime_sum += n
    g += 1
print(prime_sum)


toc = time.perf_counter()
print(f"Performed in {toc - tic:.4f} seconds")