# Домашняя работа 5.
# Задача 1.
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))
def f(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * f(a, b - 1))
print('Ответ:', f(a, b))

# Задача 2.
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input('Введите целое неотрицательное число a: '))
b = int(input('Введите целое неотрицательное число b: '))
def f(a, b):
    a += 1
    b -= 1
    if b > 0:
        return f(a, b)
    else:
        return a
print('Ответ:', f(a, b))