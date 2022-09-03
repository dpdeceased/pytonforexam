n = int(input())
count = 0
if n < 1:
    print('Ваше число слишком маленькое!')
if n > 10:
    print('Ваше число слишком большое!')
else:
    while n <= 1000:
        n *= 7
        count += 1
print(count)