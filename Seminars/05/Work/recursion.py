from random import randint
import sys

def rev(n):
    if n == 0: return ''
    num = input()
    return rev(n - 1) + f' {num}'


def rev1(n):
    if n == 0: return 0
    num = randint(1, 100)
    return f'{rev1(n - 1)} {num}'

print(rev1(995))
# sys.setrecursionlimit(15000)
print(rev1(10000))
