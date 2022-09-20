n = int(input())
a = [int(input()) for i in range(n)]
k = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] * a[j] % 6 == 0):
            if (a[i] + a[j]) % 100 == 0:
                k += 1
print(k)