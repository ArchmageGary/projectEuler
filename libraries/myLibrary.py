
def prime_check(x):
    prime = True
    for i in range(2, int((x/2) +1)):
        if x%i == 0:
            prime = False
    return prime



# timer function
# import time
# tic = time.perf_counter()

# toc = time.perf_counter()
# print(f"Performed in {toc - tic:.4f} seconds")

