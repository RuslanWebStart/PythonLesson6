# -*- coding: cp1251 -*-

# ���� 6

# ������ 1
N = int(input('������� ���������� �����: '))
quantity = 0

for i in range(N):
    n = int(input('������� �����: '))

    if n == 0:
        quantity += 1

print('����� ������ 0:', quantity)



# ������ 2
X = int(input('������� ����������� �����: '))
counter = 0

for i in range(1, X + 1):
    if X % i == 0:
        counter += 1

print('���������� ����������� ���������: ', counter)



# ������ 3
print('������� ����� ����� � ������� = ��� < ����� �')
A = int(input('����� �: '))
B = int(input('����� �: '))
segment = ''

for i in range(A, B + 1):
    if i % 2 == 0:
        segment += str(i) + ' '

print('������ ����� ������� �� � �� �:', segment )