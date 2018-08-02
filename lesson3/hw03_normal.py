import math


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fib_list = [1, 1]
    for i in range(1, m):
        fib_list.append(fib_list[i] + fib_list[i - 1])

    return fib_list[n - 1: m]


print(fibonacci(3, 10))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1

    print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(condition, *args):
    lst = []

    for i in args:
        if i != condition:
            lst.append(i)

    return lst


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def get_length(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def check_para(a1, a2, a3, a4):
    a1_a2 = get_length(a1, a2)
    a3_a4 = get_length(a3, a4)
    a1_a3 = get_length(a1, a3)
    a2_a4 = get_length(a2, a4)
    if a1_a2 == a3_a4 and a1_a3 == a2_a4:
        return 'Является паралелограммом'
    else:
        return 'не является паралелограммом'


A1 = (1, 3)
A3 = (-1, 4)
A2 = (4, 7)
A4 = (2, 8)

print(check_para(A1, A2, A3, A4))
