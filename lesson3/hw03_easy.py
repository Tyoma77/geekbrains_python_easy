# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    tmp_list = str(number).split('.')
    f_digit = int(tmp_list[0])
    s_digit = 0

    for i in range(0, ndigits):
        s_digit += int((tmp_list[1])[i]) / (10 ** (i + 1))
        if i == ndigits - 1:
            if int((tmp_list[1])[i+1]) >= 5:
                s_digit += 1 / (10 ** (i + 1))

    digit = s_digit + f_digit
    return digit


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6:
        return "Номер не шестизначный"
    t1 = 0
    t2 = 0

    ticket_list = str(ticket_number)

    for i in range(0, 2):
        t1 += int(ticket_list[i])
        t2 += int(ticket_list[i + 2])

    if t1 == t2:
        return "Счастливый"
    else:
        return "Несчастливый"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
