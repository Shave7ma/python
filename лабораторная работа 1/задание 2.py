# Дана строка, в которой необходимо найти общее количество русских символов

if n == 1:
    print(u'Введите строку: ')
    x = input()
    c = 0
    for i in x:
        if ord(i) == 1025 or ord(i) >= 1040 and ord(i) <= 1103 or ord(i) == 1105:
            c += 1
    print(u'Количество русских символов в строке: ', c)

#Дана строка, в которой необходимо проверить, образуют ли строчные символы латиницы палином
    
if n == 2:
    lat = ""
    for i in x:
        if ord(i) >= 97 and ord(i) <= 122:
            lat += i
    str = "".join(reversed(lat))
    print(u'Строчные символы латиницы из исходной строки: ', lat)
    if lat == str:
        print(u'Это палином!')
    else:
        print(u'Это не палином :(')
