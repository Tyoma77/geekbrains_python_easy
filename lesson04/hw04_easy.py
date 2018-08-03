# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


def first(li):
    n_list = [i ** 2 for i in li]
    return n_list


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def second(fst_list, scn_list):
    unique = [str(i).lower() for i in fst_list] + [str(j).lower() for j in scn_list]
    unique = list(set(unique))
    return unique


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def third(numb_list):
    unique_num_list = [i for i in numb_list if i % 3 == 0 and i > 0 and i % 4 != 0]
    return unique_num_list


if __name__ == "__main__":
    print(first([1, 2, 4, 0]))

    list_1 = ['asdasdad', 'asdasda']
    list_2 = ['asdasdasdasdc', 'aasdasdasdfxv', 'asdasda']
    print(second(list_1, list_2))

    num_list = [i for i in range(-5, 45)]
    print(third(num_list))
