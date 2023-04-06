# #### 6.2[32]: Напишите функцию ```print_operation_table(operation, num_rows=6, num_columns=6)```, которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. Аргументы ```num_rows``` и ```num_columns``` указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.

# 	Примеры/Тесты:
#     print_operation_table(lambda x,y: x**y,4,4)
# 	1   1   1   1
# 	2   4   8  16
# 	3   9  27  81
# 	4  16  64 256

#     print_operation_table(lambda x,y: x*y)
# 	1   2   3   4   5   6
# 	2   4   6   8  10  12
# 	3   6   9  12  15  18
# 	4   8  12  16  20  24
# 	5  10  15  20  25  30
# 	6  12  18  24  30  36


# ```(*)``` **Усложнение.** Сформируйте форматированный вывод с номерами строк и столбцов

# 	Примеры/Тесты:
# 	print_operation_table(lambda x,y: x**y,4,4)
# 	       1   2   3   4
# 	    ----------------
# 	1 |    1   1   1   1
# 	2 |    2   4   8  16
# 	3 |    3   9  27  81
# 	4 |    4  16  64 256

# 	print_operation_table(lambda x,y: x*y)
# 	       1   2   3   4   5   6
# 	    ------------------------
# 	1 |    1   2   3   4   5   6
# 	2 |    2   4   6   8  10  12
# 	3 |    3   6   9  12  15  18
# 	4 |    4   8  12  16  20  24
# 	5 |    5  10  15  20  25  30
# 	6 |    6  12  18  24  30  36


def print_operation_table(operation, num_rows=6, num_columns=6):
    space_count = 6
    tab = '\t'

    # table = [[0] * num_rows] * num_columns
    table = [[str(operation(x + 1 , y + 1)) for y in range(num_columns)] for x in range(num_rows)]
    # print(table)

    th_number = ["\t" + str(y + 1) for y in range(num_columns)]
    print(*th_number)
    th_line = ''.join(["-" * (space_count + len(str(y))) for y in range(num_columns)])
    print(f'{tab}{th_line}')
    for x in range(num_rows):
        print(f'{x + 1} | {tab}{tab.join(table[x])}')

    print('\n')



print_operation_table(lambda x,y: x**y,4,4)

print_operation_table(lambda x,y: x**y,3,12)

print_operation_table(lambda x,y: x*y)




# def print_operation_table(operation, num_rows=6, num_columns=6):
#     space_count = len(str(operation(num_rows, num_columns))) + 2
#     space_corner = 5

#     # table = [[0] * num_rows] * num_columns
#     table = [[str(operation(x + 1 , y + 1)) for y in range(num_columns)] for x in range(num_rows)]

#     th_number = ''.join([" " * (num_columns - len(str(y + 1))) + str(y + 1) for y in range(num_columns)])
#     print(th_number)

#     th_line = ''.join([("-" * (space_count + len(str(y)))) for y in range(num_columns)])
#     print(f'{" " * space_corner}{th_line}')

#     for x in range(num_rows):
#         prefix = f'{x + 1} |  '
#         # print(f'{space_count} - {len(table[x])} x = {table[x]}')
#         print(f'{prefix}{" " * (space_corner - len(prefix))}{(" " * (space_count)).join(table[x])}')

#     print('\n')



# print_operation_table(lambda x,y: x**y,4,4)

# print_operation_table(lambda x,y: x**y,3,12)

# print_operation_table(lambda x,y: x*y)
