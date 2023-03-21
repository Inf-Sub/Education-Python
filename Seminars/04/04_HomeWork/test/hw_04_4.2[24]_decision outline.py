# #### 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке 
# растет N кустов. Собирающий модуль за один заход, находясь непосредственно 
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом. 
# На входе задано количество ягод на каждом кусте. Не обязательно вводить 
# их с клавиатуры, можно задать непосредственно в коде программы

#     Примеры/Тесты:
#     Input1: 1, 2, 3, 4, 5, 6, 7, 8
#     Output1: Макс. кол-во ягод 21, собрано для куста 7

#     Input1: 11, 92, 1, 42, 15, 12, 11, 81
#     Output1: Макс. кол-во ягод 184, собрано для куста 1

blueberry = [11, 92, 1, 42, 15, 12, 11, 81]
blueberry = [1, 2, 3, 4, 5, 6, 7, 8]
max_bushes_at_time = 3
max_bush = len(blueberry)
half_max_bushes = max_bushes_at_time
best_bush = 0
max_berry = 0

for bush in range(max_bushes_at_time):    
    max_berry += blueberry[bush]    
    current_sum = max_berry

# for bush, berries in enumerate(blueberry):
for bush in range(max_bush - half_max_bushes):
    current_bush = (bush + max_bushes_at_time) % max_bush
    # print(bush, berry)
    print(f'{bush}, {bush + max_bushes_at_time} == {current_bush}')
    # print(f'{bush}, {current_sum} - {blueberry[bush]} + {blueberry[(bush + max_bushes_at_time) % max_bush]}')
    current_sum = current_sum - blueberry[bush] + blueberry[current_bush]
    if current_sum >= max_berry:
        max_berry = current_sum
        best_bush = current_bush if current_bush else max_bush
        

    print(f'{bush} {current_sum}\t{best_bush}\t{max_berry}')


print(f'Макс. кол-во ягод {max_berry}, собрано для куста {best_bush}')

    # if not bush:    # 0
    #     left = blueberry[-1]
    #     right = blueberry[bush + 1]
    #     current = left + center + right
    #     print(f'{bush} ({left}, {center}, {right})\t{current}\t{best_bush}\t{max_berry}')

    # if bush and bush < max_bush:
    #     right = blueberry[bush + 1]
    #     current += right - left
    #     left = blueberry[bush - 1]
    #     print(f'{bush} ({left}, {center}, {right})\t{current}\t{best_bush}\t{max_berry}')



    # if bush and bush < max_bush:
    #     left = blueberry[bush - 1]
    #     right = blueberry[bush + 1]
    #     print(f'{bush} ({left}, {center}, {right})\t\t{best_bush}\t{max_berry}')
    # elif not bush:
    #     left = blueberry[-1]
    #     right = blueberry[bush + 1]
    #     print(f'{bush} ({left}, {center}, {right})\t\t{best_bush}\t{max_berry}')
    # else:
    #     left = blueberry[bush - 1]
    #     right = blueberry[0]
    #     print(f'{bush} ({left}, {center}, {right})\t\t{best_bush}\t{max_berry}')

