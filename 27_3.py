# На вход подается натуральное число n и n целых чисел. Напишите программу,
# которая выводит наименьшее из этих чисел.

n = int(input())  #вводим с клавиатуры количиство n целых чисел
minim = 100000000000  # переменная мин чтоб х был меньше так и так
for i in range(n):  # тут от 1 до n цикл
    x = int(input())  #вводим n раз х
    if x < minim:  #если наш х < миллона миллионов
        minim = x  #тогда мы в миним записываем наш х и икл повторяется, если второе число будет больше чем первое оно не запишится )
print(minim)