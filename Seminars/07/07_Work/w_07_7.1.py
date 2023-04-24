# №7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич

# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович

# 2) записать эти данные в список  вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием
# os.path и pathlib

from os.path import join, abspath

datapath = join('.', 'data')
filename = join(datapath, 'w_07_7.1_data.csv')

print(filename)
print(abspath(filename))

# file = open('w_07_7.1_data.csv', mode='r', encoding='utf-8')
file = open(filename, mode='r', encoding='utf-8')
# for line in file:
#     print(line.strip())
data = [el.strip().split('#') for el in file]
print(data)

file.close()
