
#Sieve of Eratosthenes


list = []
d = 110000
for i in range(2, d+1):
    list.append(i)


for s in range(2, len(list)):
    for i in range(s, int((d/s)+1)):
        if int(s*i) in list:
            list.remove(int(s * i))

print(len(list))
print(list[10000])