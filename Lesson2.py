# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть
import random
n = int(input())
spisok = []
for i in range(n):
    i = random.randint(0,1)
    spisok.append(i)
    
# print(spisok)
if spisok.count(0) < spisok.count(1):
    print(spisok.count(0))
else:
    print(spisok.count(1))
# k = 0
# for i in range(n):
#     v = random.randint(0,1)
#     if v == 1:
#         k += 1

# print(k if k<n/2 else n-k)
