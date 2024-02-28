int_list = []
print(u'Вводите элементы. Учтите, что нецелочисленные значения игнорируются. Для завершения дважды нажмите Enter:')
temp = input()

while(len(temp) > 0):
    if temp.isdigit() or temp[0] == '-' and temp[1:len(temp)].isdigit():
        int_list.append(int(temp))
    temp = input()

print(u'Исходный массив:')
for i in int_list:
    print(i)

#Найти количество элементов, расположенных после последнего максимального

def find_last_max(x):
    last_max = x[0]
    last_max_index = 0
    for i in range(0, len(x)):
        if x[i] >= last_max:
            last_max = x[i]
            last_max_index = i
    return last_max_index

def amount_of_elements_after(x, after_what):
    if after_what < len(x):
        return len(x[after_what + 1 : len(x)])
    else:
        return 0

print(u'\nКоличество элементов после последнего максимального:', amount_of_elements_after(int_list, find_last_max(int_list)))

#Переместить все элементы, расположенные до минимального, в конец массива

def all_elems_after_min(x):
    minimum = min(x)
    i = 0
    while i < len(x):
        if x[i] != minimum:
            x.append(x[i])
            x.pop(i)
        else:
            break     
    return x

if (int_list.count(min(int_list)) != 1):
    print(u'\nМинимальный элемент встречается больше одного раза, по условию задачи такого быть не должно!')
else:
    print(u'\nСписок, но все элементы до минимального теперь в конце:')
    int_list = all_elems_after_min(int_list)
    for i in int_list:
        print(i, end = ' ')

#Найти максимальный из элементов на интервале [a,b]

print(u'\n\nВведите целочисленное a:')
a = int(input())
print(u'Введите целочисленное b:')
b = int(input())

def find_max_on_interval(x, a, b):
    interval_list = list(filter(lambda k: k <= b and k >= a, x))
    if len(interval_list):
        return max(interval_list)
    else:
        return 'no'
            
maximum_on_interval = find_max_on_interval(int_list, a, b)
if maximum_on_interval != 'no':
    print(u'Максимум на интервале [', a, u',', b, ']: ', maximum_on_interval)
else:
    print(u'Нет элементов, принадлежащих этому интервалу :(')

#Вывести индексы элементов, которые меньше левого соседа, и количество таких чисел
    
def indexes(x):
    indexes = []
    for i in range (1, len(x)):
        if x[i] < x[i-1]:
            indexes.append(i)
    return indexes

index_list = indexes(int_list)

print(u'\n\nВсе индексы элементов, которые меньше левого соседа:')
for i in index_list:
    print(i, end =' ')
print(u'\nИх количество:', len(index_list))

#Для введенного списка положительных чисел построить список всех положительных простых делителей элементов списка без повторений

def is_prime(n):
    if n == 2:
        return n
    else:
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                return 0
    return n

def creating_set(x):
    a = set()
    for elem in x:
        for i in range(2, elem):
            if elem % i == 0 and is_prime(i):
                a.add(i)
    return a

set_of_prime_dels = creating_set(int_list)
print(u'Список всех простых делителей:')
for i in set_of_prime_dels:
    print(i, end = ' ')
