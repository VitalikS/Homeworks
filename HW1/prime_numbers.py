m = int(input('m='))
n = int(input('n='))
a = list(range(n + 1))
a[1] = 0
list = []

i = 2
while i <= n:
    if a[i] != 0:
        list.append(a[i])
        for j in range(i, n + 1, i):
            a[j] = 0
    else:
        i += 1

k = 0
while k < 1:
    if list[k] < m:
        list.remove(list[k])
    else:
        k += 1
print(list)