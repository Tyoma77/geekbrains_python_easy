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
    def __init__(self, name, surname, patronymic, subject, *classes):
        super().__init__(name, surname, patronymic)
        self.subject = subject
        self.classes = [elm for elm in classes]
    
    @classmethod
    def the_same_subject(cls, *args):
        for i in range(len(args[0])):
            for j in range(i + 1, len(args[0])):
                elem1 = args[0][i]
                elem2 = args[0][j]
                if not (elem1.get_full_name is elem2.get_full_name) and (elem1.subject is elem2.subject):
                    classes = list(set(elem1.classes).union(elem2.classes))
                    if len(classes) < len(elem1.classes) + len(elem2.classes):
                        same_classes = []
                        for cls1 in elem1.classes:
                            for cls2 in elem2.classes:
                                if cls1 is cls2:
                                    same_classes.append(cls1)
                        print(f' {elem1.get_full_name()} и {elem2.get_full_name()}')
                        print(f' преподают один и тот же предмет: {elem1.subject} в ' + ', '.join(same_classes))
    


if __name__ == '__main__':
    
    mather1 = Human("Алиса", "Васильевна", "Селезнева")
    mather2 = Human("Алина", "Николаевна", "Зайцева")
    mather3 = Human("Екатерина", "Ивановна", "Банных")
    mather4 = Human("Наталья", "Васильевна", "Иванова")
    mather5 = Human("Татьяна", "Вячеславовна", "Петрова")
    mather6 = Human("Анна", "Сергеевна", "Сидорова")
    father1 = Human("Алексей", "Вячеславович", "Селезнев")
    father2 = Human("Иван", "Александрович", "Зайцев")
    father3 = Human("Александр", "Юрьевич", "Банных")
    father4 = Human("Юрий", "Петрович", "Иванов")
    father5 = Human("Вадим", "Николаевич", "Петров")
    father6 = Human("Александр", "Петрович", "Сидоров")
    
    students = [Student("Александр", "Алексеевич", "Селезнев", "5 А", mather1, father1),
          Student("Алла", "Ивановна", "Зайцева", "5 А", mather2, father2),
          Student("Светлана", "Александровна", "Банных", "6 Б", mather3, father3),
          Student("Кирилл", "Юрьевич", "Иванов", "7 А", mather4, father4),
          Student("Николай", "Вадимович", "Петров", "8 Б", mather5, father5),
          Student("Вячеслав", "Александрович", "Видоров", "4 В", mather6, father6)]
    
    teachers = [Teacher("Елена", "Антониновна", "Снытко", "Русский язык", '5 А', '5 Б', '5 В'),
                Teacher("Сергей", "Викторович", "Сизый", "Физика", '7 А', '7 Б', '7 В'),
                Teacher("Александр", "Анатольевич", "Макаров", "Информатика", '7 А', '7 Б', '7 В'),
                Teacher("Екатерина", "Владимировна", "Елфимова", "Математика", '5 А', '6 Б', '5 В'),
                Teacher("Степан", "Владиславович ", "Корявов", "Физика", '7 А', '8 Б', '7 В'),
                Teacher("Филимон", "Михеевич", "Демченко", "Математика", '5 А', '4 Б', '4 В')]
    
    class_list = []
    for tch in teachers:
        class_list = list(set(class_list).union(tch.classes))
    for std in students:
        if std.class_room not in class_list:
            class_list.append(std.class_room)
    print('Полный список всех классов школы: ' + ', '.join(sorted(class_list)))
    print()
    
    class_room = '5 А'
    print(f'Ученики {class_room}:')
    for std in students:
        if std.class_room == class_room:
            print(std.get_full_name())
    print()
    print('Учителя, преподающие в {}:'.format(class_room))
    
    for tch in teachers:
        if class_room in tch.classes:
            print(tch.get_full_name())
    print()

    std = students[3]
    print(std.get_full_name())
    print(std.get_parents())
    print('Изучаемые предметы:')
    for std in teachers:
        if pup.class_room in tch.classes:
            print(tch.subject)
