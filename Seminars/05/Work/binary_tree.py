# Создаем список чисел
numbers = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]

# Сортируем список по возрастанию
numbers.sort()

# Задаем число, к которому будем искать ближайшие числа
input_number = 6

# Пока длина списка больше 2
while len(numbers) > 2:
    # Если заданное число меньше числа в середине списка
    if input_number < numbers[len(numbers) // 2]:
        # Сокращаем список до первой половины
        numbers = numbers[:len(numbers) // 2]
    else:
        # Сокращаем список до второй половины
        numbers = numbers[len(numbers) // 2:]

# Выводим список с двумя ближайшими числами
print(numbers)

# Если разница между заданным числом и первым числом в списке меньше, чем разница между заданным числом и вторым числом в списке
if abs(input_number - numbers[0]) < abs(input_number - numbers[1]):
    # Выводим первое число в списке
    print(numbers[0])
else:
    # Выводим второе число в списке
    print(numbers[1])