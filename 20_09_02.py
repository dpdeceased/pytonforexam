f = open('file2__t5ed.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
print(a)
m = -10000000000000000
for x in range(len(a)):
    if(a[i] > m):
        m = a[i]
print(m)