# -*- coding: cp1251 -*-

# Урок 6

# Задача 1
N = int(input('Введите количество чисел: '))
quantity = 0

for i in range(N):
    n = int(input('Введите число: '))

    if n == 0:
        quantity += 1

print('Чисел равных 0:', quantity)



# Задача 2
X = int(input('Введите натуральное число: '))
counter = 0

for i in range(1, X + 1):
    if X % i == 0:
        counter += 1

print('Количество натуральных делителей: ', counter)



# Задача 3
print('Введите целое число А которое = или < числа В')
A = int(input('Число А: '))
B = int(input('Число В: '))
segment = ''

for i in range(A, B + 1):
    if i % 2 == 0:
        segment += str(i) + ' '

print('Четные числа отрезка от А до В:', segment )