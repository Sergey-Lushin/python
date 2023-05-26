#lambda, filter, map, zip, enumerate, list comprehension

#list comprehension
# a = [i if i < 3 else 0 for i in range(5)]
# print(a)
# for i in range(6):
#     a.append(5)
# print(a)

#enumerate
# a = [0, 1, 2, 3, 2, 5, 1]
# for indx,val in enumerate(a):
#     print(indx,val)

#zip
# a = (1,2,4,5,6)
# b = "abcd"
# f = {45:"b",54:"c",87:"fr"}
# for i1,i2,i3 in zip(a,b,f.values()):
#     print(i1,i2,i3)

#lambda

# def summa(a,b):
#     return a+b
#
# a = lambda x,y: x+y if x == 3 else 0

#map
# a = [1,2,3,4,5,6]
# a = list(map(lambda el: el if el%2==0 else 0,a))
# print(a)

#filter
# a = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda el: True if el%2==0 else False,a))
# print(a)

#Задача 47: У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = lambda x: x
transormed_values = list(map(transformation, values))


# Задача 49: Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
#  орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), 
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые 
# орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины 
# полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары 
# чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины 
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет 
# найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
#  имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна

def find_farthest_orbit(list_of_orbits):
    s = []
    for i in list_of_orbits:
        if i[0] != i[1]:
            s.append(i[1] * i[0])
        res = s.index(max(s)) 
    return list_of_orbits[res]
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

#Задача 51: Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты 
# имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение 
# характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна
#  возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его
#  характеристику.

values = [0, 2, 10, 6, 7]
def same_by(characteristic, objects): 
    return(len(list(filter(characteristic, objects)))) == 0
if same_by(lambda x: x % 2, values):
	print("same")
else:
	print("different")




