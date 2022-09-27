#a = int(input())
#b = int(input())
#c = int(input())
#sum = (a + b + c)
#umn = (a * b * c)
#print(sum, umn)

x = int(input())
a = x % 10
b = x // 100
c = x % 100 // 10
sum = (a + b + c)
umn = (a * b * c)
print(sum, umn)
