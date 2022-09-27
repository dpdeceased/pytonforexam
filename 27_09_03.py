n = int(input())
a = []
x = 1
for i in range(1, n + 1):
    a.append(i)
for i in range(len(a)):
    x = x * a[i]
print(x)