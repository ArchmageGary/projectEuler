
def primeCheck(x):
    prime = True
    for i in range(2, int((x/2) +1)):
        if x%i == 0:
            prime = False
    return prime


x = 4

print(primeCheck(x))