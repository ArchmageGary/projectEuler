import time
tic = time.perf_counter()

#This is a Fibonacci sequence problem
array = [1,1]
total = 2

#Build a self-expanding array.
n = 3

while len(array) < n:
    array2 = []
    array2.append(1)
    for g in range((len(array)-1)):
        array2.append(array[g]+array[g+1])
    array2.append(1)
    array = array2
    total += sum(array)
print(array)
print(total)


toc = time.perf_counter()
print(f"Performed in {toc - tic:.4f} seconds")