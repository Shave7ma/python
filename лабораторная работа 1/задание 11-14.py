import re

string_list = []
print(u'Сколько строк вы собираетесь добавить?')
n = int(input())
for i in range(n):
    string_list.append(input())

#Отсортировать строки в порядке увеличения разницы между количеством согласных и количеством гласных букв в строке

string_list.sort(key = lambda stroke: len(re.findall(r'[ёуеыаоэяию]', stroke, re.IGNORECASE)) - 
len(re.findall(r'[йцкнгшщзхъфвпрлджчсмтьб]', stroke, re.IGNORECASE)), reverse = True) #английские буквы вводить не хочу, хоть и могу!

print(u'Строки, отсортированные по разнице между количеством согласных и гласных:')
for i in string_list:
    print(i)

#Отсортировать строки в порядке увеличения квадратичного отклонения среднего веса символа строки от среднего веса символа первой строки
    
def quad_dev(x, av_first):
    numerator = 0
    amount = 0
    for i in range(len(x)):
        numerator += (ord(x[i]) - av_first)**2
        amount += 1
    return (numerator / amount)**0.5

def average_of_first_row(x):
    total_weight = 0
    amount = 0
    for i in range(len(x)):
        total_weight += ord(x[i])
        amount += 1
    return total_weight / amount

av = average_of_first_row(string_list[0])
string_list.sort(key = lambda stroke: quad_dev(stroke, av))

print(u'Строки, отсортированные в порядке, который я не хочу подробно описывать:')
for i in string_list:
    print(i)
    
#Отсортировать строки в порядке увеличения разницы между количеством сочетаний "гласная-согласная" и "согласная-гласная"

gl_sogl = r'[ёуеыаоэяию][йцкнгшщзхъфвпрлджчсмтьб]'
sogl_gl = r'[йцкнгшщзхъфвпрлджчсмтьб][ёуеыаоэяию]'

string_list.sort(key = lambda stroke: len(re.findall(gl_sogl, stroke, re.IGNORECASE)) - len(re.findall(sogl_gl, stroke, re.IGNORECASE)), reverse = True)

print(u'Строки, отсортированные в порядке увеличения разницы между количеством "гл-согл" и "согл-гл": ')
for i in string_list:
    print(i)

#Отсортировать строки в порядке увеличения количества "зеркальных" троек в строке
    
def amount_of_trio(x):
    amount = 0
    for i in range (0,len(x)-2):
        if x[i] == x[i+2] and x[i] != x[i+1]:
            amount += 1
    return amount

string_list.sort(key = lambda st: amount_of_trio(st))

print(u'Строки, отсортированные в порядке увеличения количества "зеркальных" троек вида aea: ')
for i in string_list:
    print(i)
