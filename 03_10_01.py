f = open('1__w42p.txt')
a = [int(i) for i in f.readlines()]
print(a)
k = 0
max = -10000000000
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if (x+y) % 2 == 0:
        k += 1
    if x > max:
        max = x
    if y > max:
        max = y

print(k,max)