#Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def degree(a, b):
    if b == 0:
        return 1
    else:
        return a * degree(a, b-1)

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

print(degree(a, b))

#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

print(sum(a, b))