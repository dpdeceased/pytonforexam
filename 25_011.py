x = 1052336
a = [1,2,98,43,89,739]
b = []
for i in range(len(a)):
    if (x % a[i] == 0):
        b.append(x // a[i])
print(sum(b))