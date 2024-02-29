string_list = []
print(u'Сколько строк вы собираетесь добавить?')
n = int(input())
print(u'Хорошо, добавляйте', n, u'строк:')
for i in range(n):
    string_list.append(input())

string_list.sort(key = lambda stroke: len(stroke.split()))
print('\nВ каком порядке вывести отсортированный список? 1 - по возрастанию количества слов, 2 - по убыванию')
n = int(input())

if n == 1:
    for i in string_list:
        print(i)
if n == 2:
    for i in reversed(string_list):
        print(i)
