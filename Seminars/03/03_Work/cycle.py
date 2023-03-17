names = range(10)

# итерируемый объект по которому мы можем пробежаться поэлементно
# последовательности: str/list/tuple/range/
# контейнеры: dict/set

for name in names:
    print(name)

for name in {1, 2, 5, 7}:
    print(name)

d1 = {"V": "S001", "X": "D009"}
# for name in d1: или
for name in d1.keys():
    print(name)

for name in d1.values():
    print(name)

# tuple from key => value
for name in d1.items():
    print(name)
    print(name[0], name[1])

# распаковка: tuple from key => value
for key, value in d1.items():
    print(f'key: {key}, value: {value}')

my_list1 = [2,324,54,676,8,4]
my_list2 = [2,324,54,676,8,4]

print(f'my_list: {my_list1.sort()}')
print(f'my_list: {my_list1}')

# print(f'my_list: {my_list2.sorted()}')