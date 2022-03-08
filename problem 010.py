
def primeCheck(x):
    prime = True
    for i in range(2, int((x/2)+1)):
        if x%i == 0:
            prime = False
    return prime

#Summation of primes
#Find the sum of all primes below 2 million
#researching wheel factorization
#Calculate first p prime numbers and perform wheel factorization automatically from there

list = []
basis = []
primes = []
d = 10
p = 2


x = 1
while len(basis) < p:
    x += 1
    if primeCheck(x) == True:
        basis.append(x)



x = 1
for i in range(0, p):
    x *= basis[i]
for i in range(2, x+2):
    if primeCheck(i):
        list.append(i)
print(list)


for i in list:
    primes.append(0)
    n = 0
    while primes[-1] < d:
        q = (list[i] + (x * n))
        n += 1
        if q < d:
            primes.append(q)
        print(primes[-1])
print(primes)
