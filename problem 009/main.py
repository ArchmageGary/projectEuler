
for i in range(1, 500):
    for g in range(i+1, 500):
        for h in range(i+2, 500):
            a = i
            b = g
            c = h
            if a+b+c > 1000:
                continue
            if a**2 + b**2 == c**2:
                if a + b + c == 1000:
                    print(a, b, c)
                    print(a*b*c)
