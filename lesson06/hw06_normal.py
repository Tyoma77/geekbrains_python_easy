# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика+
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return '{} {} {}'.format(self.surname, self.name, self.patronymic)

    def get_small_name(self):
        return '{} {}. {}.'.format(self.surname, self.name[0], self.patronymic[0])


class Student(Human):
    def __init__(self, name, surname, patronymic, father, mother, group):
        super().__init__(name, surname, patronymic)
        self.father = father
        self.mother = mother
        self.group = group

    def get_parents(self):
        return 'Мать: {}, отец: {}'.format(self.mother.get_small_name(), self.father.get_small_name())


class Teacher(Human):
    def __init__(self, name, surname, patronymic, subject):
        super().__init__(name, surname, patronymic)
        self.subject = subject


if __name__ == '__main__':
    students = []
    teachers = []

    # TODO 1. Получить полный список всех классов школы
    # TODO 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
    # TODO 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
    # TODO 5. Получить список всех Учителей, преподающих в указанном классе

    # 4.
    for s in students:
        print(s.get_parents())
