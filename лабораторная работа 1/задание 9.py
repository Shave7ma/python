string_list = []
print(u'Сколько строк вы собираетесь добавить?')
n = int(input())
for i in range(n):
    string_list.append(input())

print(u'В каком порядке вы хотите вывести список? 1 - по возрастанию, 2 - по убыванию')
k = int(input())

if k == 1:
    string_list.sort(key = len)
    for i in string_list:
        print(i)
elif k == 2:
    string_list.sort(key = len, reverse = True)
    for i in string_list:
        print(i)
