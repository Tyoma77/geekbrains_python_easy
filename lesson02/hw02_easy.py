import random

def create_list(x):
	tmp_list = []
	while  x > 0:
		tmp_list.append(random.randint(1, 20))
		x -= 1
	return tmp_list

# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка выровненного по правой сторне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: использует метод .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 0
while i < len(fruits):
    print('{}. {:>7}'.format(i+1, fruits[i]))
    i += 1

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке

list_1 = []
list_2 = []

list_1 = create_list(random.randint(2, 10))
list_2 = create_list(random.randint(2, 10))

for k in list_2:
	while list_1.count(k) > 0:
		list_1.remove(k)
		
print(list_1)
print(list_2)


# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного выполнив следующие условия:
# если элемент кратный двум, то разделить его на 4, если не кратен, то умножить на два.

num_list = create_list(random.randint(2, 10))
new_num_list = []

for num in num_list:
    if num % 2 == 0:
        new_num_list.append(num / 4)
    else:
        new_num_list.append(num * 2)
print(num_list)
print(new_num_list)
