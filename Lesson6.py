#Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
#разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d. Каждое число вводится с новой строки.

first_element = int(input("Enter the first element: "))
difference = int(input("Enter the difference: "))
number_of_elements = int(input("Enter the number of elements: "))

arithmetic_progression = [first_element + i * difference for i in range(number_of_elements)]

print(arithmetic_progression)

#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
array = [1, 2, 3, 4, 5]
minimum = int(input("Enter the minimum value: "))
maximum = int(input("Enter the maximum value: "))

indices = [i for i, x in enumerate(array) if minimum <= x <= maximum]

print(indices)