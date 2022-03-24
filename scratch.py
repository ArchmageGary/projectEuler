def coprime_check(basis, x):
    coprime = True
    for i in basis:
        if x%i == 0:
            coprime = False
            break
    return(coprime)

basis = [2,3,5]
x = 30
columns = []

for i in range(30,60):
    if coprime_check(basis,i):
        columns.append(i-x)
print(columns)