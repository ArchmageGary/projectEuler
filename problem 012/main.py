import time
tic = time.perf_counter()

def triangle_generator(x):
    return(int((x**2 + x)/2))

def divisor_counter(x):
    counter = 0
    for i in range(1,int(x/2+1)):
        if x%i == 0:
            counter += 1
    return counter

d = 500

counter = 0
x = 1
while counter < d:
    x += 1
    counter = divisor_counter(triangle_generator(x))

print(triangle_generator(x))



toc = time.perf_counter()
print(f"Performed in {toc - tic:.4f} seconds")