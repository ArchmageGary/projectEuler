from libraries.myLibrary import *

array = [1,1]

array2 = []
array2.append(1)
for g in range((len(array)-1)):
    array2.append(array[g-1]+array[g])
array2.append(1)
array = array2

print(array2)