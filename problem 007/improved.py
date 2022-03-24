import time
tic = time.perf_counter()

def prime_check(x):
    prime = True
    for i in range(2, int((x/2) +1)):
        if x%i == 0:
            prime = False
    return prime

def coprime_check(basis, x):
    coprime = True
    for i in basis:
        if x%i == 0:
            coprime = False
            break
    return(coprime)

basis = [2, 3, 5]
w = 30

primes = []
columns = []

for i in range(2, 2*w):
    if prime_check(i):
        primes.append(i)

for i in range(w+1, 2*w):
    if coprime_check(basis, i):
        columns.append(i-w)

g = 1
n = 2*w
while n < 110000:
    g += 1
    for i in columns:
        if coprime_check(basis, g*w+i):
            primes.append(g*w+i)

print(primes(10000))
toc = time.perf_counter()
print(f"Performed in {toc - tic:.4f} seconds")
