a = [5, 10, 5, 8, 5, 7, 3, 8, 0]
k = 0
m = -10000000000000000
for i in range(len(a)):
    k += (a[i] % 2 == 0)
for i in range(len(a)):
    m = max(m, a[i] * (a[i] % 2 == 0))

print(k, m,)
