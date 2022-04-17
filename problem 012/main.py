import time
tic = time.perf_counter()
import sys
sys.path.append("C://Users//jrpyles//Desktop//projectEuler//libraries")
from myLibrary import prime_check

def triangle_generator(x):
    return(int((x**2 + x)/2))


#Performs prime factorization 
def prime_factorization(x):
    prime = 1
    factors = []
    while prime < (x+2)/2:
        prime += 1
        if prime_check(prime):
            if x%prime == 0:
                factors.append(prime)
    return factors 

print(prime_factorization(15))



toc = time.perf_counter()
print(f"Performed in {toc - tic:.4f} seconds")