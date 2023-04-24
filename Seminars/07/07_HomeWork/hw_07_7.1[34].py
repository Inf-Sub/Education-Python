# #### 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.

# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False

# 	Примеры/Тесты:
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

# **Примечание.**

# - Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
# - Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.

# ```(*)``` **Усложнение.**

# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах. Эта информация возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.

# 	Примеры/Тесты:
# 		<function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])


def rhythm(poem: str, details: bool = True, vowels: str = 'аиеёоуыэюя') -> bool:
    list_poem = poem.lower().split()
    list_result = [{}] * len(list_poem)
    phrase_count = [0] * len(list_poem)

    for index, phrase in enumerate(list_poem):
        phrase_count[index] = 0
        list_result[index] = {}
        for char in vowels:
            char_count = phrase.count(char)
            if char_count:
                phrase_count[index] += char_count
                list_result[index][char] = char_count

    bool_result = True if len(set(phrase_count)) == 1 else False

    return (bool_result, list_result) if details else bool_result

print(f'Test 1:')
print(f'{rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", False)}')
print(f'{rhythm("пара-ра-рам рам-пум-пупам па-ре-по-дам", False)}')
print(f'{rhythm("пара-ра-рам рам-пуум-пупам па-ре-по-дам", False)}')
print(f'{rhythm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па", False)}')
print(f'{rhythm("Пам-парам-пурум Пум-пурум-карам", False)}')
print(f'')
print(f'Test 2:')
print(f'{rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", False)}')
print(f'{rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", True)}')
print(f'{rhythm("пара-ра-рам рам-пум-пупам па-ре-по-дам")}')
print(f'{rhythm("пара-ра-рам рам-пуум-пупам па-ре-по-дам")}')
print(f'{rhythm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па")}')
print(f'{rhythm("Пам-парам-пурум Пум-пурум-карам")}')
print(f'{rhythm("Пам-парам-пурум Пум-пурум-карам")}')