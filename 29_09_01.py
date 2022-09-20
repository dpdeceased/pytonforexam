f = open('file1__t5eb.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
m = 1000000000000000000
for i in range(len(a)):
    if a[i] < m:
        m = a[i]
print(m)