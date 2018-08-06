import re
import random
import os


# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

UP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def first_with_re(ln):
    new_line = re.split('[A-Z]', ln)
    new_line = [i for i in new_line if i != '']
    return new_line


def fist_wo_re(ln):
    for j in range(0, len(ln)):
        if ln[j] in UP:
            ln = ln.replace(ln[j], ' ')
  
    s = ln.split(' ')
    s = [i for i in s if i != '']
  
    return s


def second_with_re(ln):
    new_line = re.findall(r'[a-z]{2}[A-Z]+[A-Z]{2}', ln)
    l1 = [re.sub('[a-z]{2}', '', i) for i in new_line]
    l2 = [re.sub('[A-Z]{2}$', '', i) for i in l1]
    return l2


def find_max_length(str_list):
    max_length = 0
    tmp_max_list = []
    for k in str_list:
        if len(k) > max_length:
            max_length = len(k)
    for l in str_list:
        if len(l) == max_length:
            tmp_max_list.append(l)
    return tmp_max_list


def write_to_file():
    str_num = ''
    for i in range(0, 2500):
        str_num += str(random.randint(0, 9))

    path = os.path.join('data', 'str_num.txt')
    directory = os.path.dirname(path)

    if os.path.exists(directory) is False:
        os.mkdir(directory)

    with open(path, 'w') as file:
        file.write(str_num)


def read_from_file():
    path = os.path.join('data', 'str_num.txt')

    try:
        with open(path, 'r') as file:
            rtr_num = file.read()
    except FileNotFoundError:
        print('File not found')

    return rtr_num


def third():
    max_list = []
    write_to_file()
    str_num = read_from_file()
    for j in range(0, 10):
        pattern = '[' + str(j) + ']' + '+'
        tmp_list = re.findall(pattern, str_num)
        m = find_max_length(tmp_list)
        max_list.append(m[0])

    tmp_max = find_max_length(max_list)

    print(tmp_max)


if __name__ == "__main__":
    line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUl' \
           'TLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLx' \
           'ooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZG' \
           'kdOaQYLVBfsGSAfJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQWrM' \
           'MsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdev' \
           'HhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQS' \
           'hTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWt' \
           'ZCEXZCnZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXBqHFjvi' \
           'huNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvd' \
           'DyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

    print(first_with_re(line))
    
    print(fist_wo_re(line))

    line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeip' \
             'EUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVfzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVj' \
             'fSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzy' \
             'tmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCf' \
             'kVIAQaAbfCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyAxDctszKjSnn' \
             'daFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxii' \
             'hwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLAL' \
             'HUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZM' \
             'WSVQyzenWoGxyGPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXiUWgsKQ' \
             'rDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

    print(second_with_re(line_2))

    third()
