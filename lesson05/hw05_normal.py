import lesson05.hw05_easy as hw
import os


# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов: 1, 3,4, программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"

# Для решения данной задачи используйте алоритмы из задания easy,
# оформленныйе в виде соответствующих функций, и импортированные в данный файл из easy.py


def ask_dir():
        print('Ведите директорию')
        name = input()
        return name


def main():
    while True:
        print("Выбирете действие: \n 1. Перейти в папку \n 2. Просмотреть содержимое текущей папки \n 3. Удалить папку"
              "\n 4. Создать папку \n 5. Выход")
        choice = int(input())
        if choice == 5:
            break
        elif choice == 1:
            os.chdir(ask_dir())
        elif choice == 2:
            hw.show_list_dir(os.getcwd())
        elif choice == 3:
            hw.create_path(ask_dir())
        elif choice == 4:
            hw.delete_path(ask_dir())
            

if __name__ == '__main__':
    main()