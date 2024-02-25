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
