#Дана строка, в которой необходимо найти все даты формата "31 февраля 2007"

import re

print(u'Введите строку: ')
x = input()
month = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
pattern = r'\d{1,2}\s(?:' + '|'.join(month) + r')\s\d{3,4}\s'   #предположим, что двузначных или пятизначных годов не будет
for i in re.findall(pattern, x):
    if int(i[0:2])<32:
        print(i)
