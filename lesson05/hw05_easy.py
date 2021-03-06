import os
import shutil
import sys


# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт отображающий папки текущей директории

# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт

def create_path(name):
    path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Папка не создана. Такая папка уже сущесвует')
    else:
        print('Успешно создана')


def delete_path(name):
    path = os.path.join(os.getcwd(), name)
    try:
        os.remove(path)
    except FileNotFoundError:
        print('Невозможно удалить. Такой папки не существует')
    except PermissionError:
        print('Невозможно удалить. У вас нет прав')
    else:
        print('Успешно удалена')


def copy_file(name):
    try:
        shutil.copy(name, 'new_file.py')
    except FileNotFoundError:
        print('Такого файла не существует')
    except PermissionError:
        print('У вас нет прав')


def show_list_dir(name):
    print(os.listdir(name))


def first():
    for i in range(9):
        name = 'dir_' + str(i + 1)
        create_path(name)

    for j in range(9):
        name = 'dir_' + str(j + 1)
        delete_path(name)


def second():
    show_list_dir(os.getcwd())


def third():
    copy_file(__file__)


if __name__ == '__main__':
    first()
    third()
    second()
