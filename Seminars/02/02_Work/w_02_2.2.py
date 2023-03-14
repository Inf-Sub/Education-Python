# №2.2[11]. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

#     Примеры/Тесты:
#     5 -> в ряду Фибоначчи 5 имеет порядковый номер 6
# a 1 2 3 4 5 6 7 8  9
# b 0 1 1 2 3 5 8 13 21

number = 0
if number == 0:
    print(f'{number} - 1')
else:
    curr = 1
    prev = 0
    
    for i in range(number + 1):
        (prev, curr) = (curr, prev + curr)
        # print(prev, end = ' ')
        if number == curr:
            print(f'{number} является {i + 3} числом')
            break
    else:
        print(f'-1')


'''
number = 0
#int(input('Введите исло: ')) 
if number == 0:
    print(f'{number} - 1')
else:
    prev = 0
    cur = 1
    #flag = False
    for i in range(number):
        tmp = cur
        cur=cur+prev
        prev = tmp
        #c, b = b, c+b
        #print(, end=' ')
        if number == cur:
            print(f'{number} является {i+3} числом')
            # flag = True 
            break
    # if not flag:
    #     print('-1')
    #     # if cur > number:
    #     #     print('-1')
    #     #     break;


    else:
        print('-1')
'''