# №7.2[###]. Продолжение предыдущей задачи
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо  преобразовать к виду:
# Иванов И.И.
# Петров П.П.

# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
#     В первый - в виде Иванов И.И.
#     Во второй - в виде Иванов-И-И

# [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять
#     Как улучшить свой код в этом случае, сделать его легко расширяемым?

from os.path import join

datapath = join('.', 'data')
filename = join(datapath, 'w_07_7.2_data.csv')

with open(filename, mode='r', encoding='utf-8') as file:
    data = [el.strip().split('#') for el in file]
    new_fio = [f'{surname} {name[0]}. {parent[0]}.' for surname, name, parent in data]
    # file.write('Привет Мир\n')

print(*new_fio)

resultpath = join('.', 'result')
resultfilename = join(resultpath, 'w_07_7.2_result.csv')
# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
with open(join(resultfilename), mode="w", encoding="utf-8") as result_file:
    [result_file.write(el+"\n") for el in new_fio]
