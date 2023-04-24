# №6.3[43] Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару,
# которую необходимо посчитать.
# Напишите функцию
#     Аргументы: список целых чисел
#     Возвращает: кол-во пар

# Примеры/Тесты:
#     <function_name>([1, 2, 3, 2, 3]) -> 2
#     <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

# def my_func(numbers: list) -> int:
#     result = 0
#     for i in numbers:
#         number = numbers.count(i)
#         if number > 1:
#             result += (number * number - 1) // 2
#             print(f'{i}, {number}, {result}, {(number * number - 1) // 2}')

#     return result


def my_func(numbers: list) -> int:
    numbers.sort()

    res = 0
    num_sum = 1
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            num_sum += 1
        else:
            res += num_sum * (num_sum - 1) // 2
            num_sum = 1
    res += num_sum * (num_sum - 1) // 2
    return res



print(my_func([1, 2, 3, 2, 3, 5]))
print(my_func([1, 2, 3, 2, 3, 3, 2, 4]))



list_1 =[1, 2, 3, 2, 3, 3, 2, 4]
def get_list(list_1):
    count = 0
    for idx in range (len(list_1)):
        el = list_1[idx]
        for idx_2 in range (idx + 1, len(list_1)):
            if el == list_1[idx_2]:
              count += 1
    return count

print(get_list(list_1))
