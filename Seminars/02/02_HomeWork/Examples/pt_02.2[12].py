"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Примеры/Тесты:
4 4 -> 2 2
5 6 -> 2 3
Здесь нудно просто решить два уравнения. Которые приведут к квадратному уравнению.
Кто не помнит - посмотрите  в сети как решать. Обойдите дополнительной проверкой возможность комплексных решений.
Можно игнорировать то, что получаться рациональные решения вместо натуральных.

Для вычисления квадратного корня используйте возведение в степень 0.5 или
[*] Усложнение: найдите самостотяельно в сети какая функция стандартной библиотеки вычисляет квадратный корень и
как до нее добраться.
"""
from math import sqrt

# Основной вариант решения
S = 5
P = 6
# Равен будет (x-y)^2 и может быть меньше нуля(комплексное)
D = S ** 2 - 4 * P
if D < 0:
    print("Таких натуральных чисел не существует")
    from cmath import sqrt
x = (-S + sqrt(D)) / (-2)
y = (-S - sqrt(D)) / (-2)
print(x,y,x+y, x*y)

# Или использовать вложенный цикл
for i in range(S):
    for j in range(P):
        if x == i + j and y == i * j:
            print(i, j)

