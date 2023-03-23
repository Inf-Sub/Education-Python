#### 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Если таких чисел нет - выдать внятное диагностическое сообщение

# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# 	Примеры/Тесты:
#     Input1: 2 4 6 8 10 12 10 8 6 4 2
#     Input2: 3 6 9 12 15 18
#     Output: 6 12     Обратите внимание: Без скобочек, в одну строку

#     Input1: 2 4 6 8 10 10 8 6 4 2
#     Input2: 3 9 12 15 18
#     Output: Повторяющихся чисел нет

input_str_1 = '2 4 6 8 10 12 10 8 6 4 2'
input_str_2 = '3 6 9 12 15 18'
# input_str_1 = '2 4 6 8 10 10 8 6 4 2'
# input_str_2 = '3 9 12 15 18'

result_set = sorted(set(input_str_1.split()).intersection(set(input_str_2.split())), reverse=True)

print(*result_set if len(result_set) > 0 else ['Повторяющихся чисел нет'])
