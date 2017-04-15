import math

m = int(input('m='))
n = int(input('n='))
a = list(range(m, n + 1, 1))

i = 0

while a[i] < n + 1:
    if math.fmod(a[i], 5) != 0:
        a.remove(a[i])
        if len(a) <= i:
            break
    else:
        i += 1

print(a)