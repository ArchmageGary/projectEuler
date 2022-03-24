
import time
tic = time.perf_counter()

print(199*500 + 333*501 - 502.5*66)

toc = time.perf_counter()
print(f"Performed in {toc - tic:0.4f} seconds")