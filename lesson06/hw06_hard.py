import os
import re
from decimal import Decimal


# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчеты заработной платы (файл "data/workers"). Рассчитайте зарплату всех работников,
# зная что они получат полный оклад, если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают удвоенную ЗП
# пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"

# С использованием классов.
# Рализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла


class Worker:
    def __init__(self, name, surname, salary, hours):
        self.name = name
        self.surname = surname
        self.salary = int(salary)
        self.hours = int(hours)

    def get_hours(self, name, surname):
        p = os.path.join('data', 'hours_of')
        with open(p, 'r', encoding='UTF-8') as f:
            ln = f.readlines()
            for j in range(1, len(ln)):
                tmp_l = re.split(r'\s+', ln[j])
                if tmp_l[0] == name and tmp_l[1] == surname:
                    return int(tmp_l[2])

    def month_payment(self, name, surname, hours, salary):
        return Decimal(Worker.get_hours(self, name, surname) / hours * salary)


if __name__ == '__main__':
    worker = []
    path = os.path.join('data', 'workers')
    with open(path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        for i in range(1, len(lines)):
            tmp_wrk = re.split(r'\s+', lines[i])
            worker.append(Worker(tmp_wrk[0], tmp_wrk[1], tmp_wrk[2], tmp_wrk[4]))
    for w in worker:
        print('Зарплата работника {} {} за месяц - {} рублей'.format(
            w.name, w.surname, w.month_payment(w.name, w.surname, w.hours, w.salary).quantize(Decimal('1.00'))))
