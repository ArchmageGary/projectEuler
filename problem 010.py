
from myLibrary import primeCheck

#Summation of primes
#Find the sum of all primes below 2 million
#researching wheel factorization
#Calculate first p prime numbers and perform wheel factorization automatically from there

basis = []
d = 10
p = 2


#Generates basis
x = 1
while len(basis) < p:
    x += 1
    if primeCheck(x) == True:
        basis.append(x)

#generate first layer of the factor wheel
x = 1
for i in range(0, p):
    x *= basis[i]


#Determine relatively prime columns.
columns = []
for i in range(x+1, 2*x):
    if primeCheck(i):
        columns.append(i-x)

#Make a list with all those numbers in the columns. Tack on your basis. Sort.
list = []
for i in columns:
    list.append(0)
    g = 1
    while i + g*x < d:
        list.append(i + g*x)
        g += 1


while list[-1] < d:
    for i in range(int(len(column))):
    g = 1
        if g * x _ column[i] < d:
            list.append(g * x + list[i])
        g += 1

print(list)

#primeCheck

#The last part

print("x is " + str(x))
print(list)