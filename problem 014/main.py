import time
tic = time.perf_counter()

p = 1000000
count_max = 1
biggest = 0

for i in range(1, p, 2):
    x = i
    count = 1
    while x > 1:
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        count += 1
    if count > count_max:
        count_max = count
        biggest = i
print(biggest, count_max)

toc = time.perf_counter()
print(f"Performed in {toc - tic:.4f} seconds")