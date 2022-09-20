f = open('file3__t5ef.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
s = 0
for i in range(len(a)):
    s = s + a[i]
print(s)