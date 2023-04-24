# #### 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Циклы использовать нельзя

# 	Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3


def sum_numbers(a: int, b: int) -> int:
    if not (a and b):
        return a if a else b

    return sum_numbers(a, b - 1) + 1

print(sum_numbers(0, 3))
