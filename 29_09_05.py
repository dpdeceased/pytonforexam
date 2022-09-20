f = open('file4__t5eg.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
k = 0
for i in range(len(a)):
    if (a[i] == 42):
        k += 1
print(k)