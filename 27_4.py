# Подается массив натуральных чисел. Найдите количество нечетных чисел. Ответ
# дайте для массива [4, 28, 0, 39, 1, 4, 4, 19, 7].

a = [4, 28, 0, 39, 1, 4, 4, 19, 7]
k = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        k += 1
print(k)
