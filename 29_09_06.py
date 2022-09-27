f = open('file5__t5eh.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
k = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        k += 1
print(k)