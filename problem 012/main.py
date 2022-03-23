import time
tic = time.perf_counter()

def triangle_generator(x):
    return(int((x**2 + x)/2))





#This needs to be more efficient. 
def divisor_counter(x):
    counter = 1
    for i in range(1,int(x/2+1)):
        if x%i == 0:
            counter += 1
    return counter

d = 500

x = 50000

print(divisor_counter(28))



toc = time.perf_counter()
print(f"Performed in {toc - tic:.4f} seconds")