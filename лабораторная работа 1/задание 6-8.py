import re

print(u'Введите строку: ')
x = input()

print(u'Какую задачу хотите решать? Введите число от 1 до 3: ')
n = int(input())

#Найти в строке максимальное из имеющихся в ней вещественных чисел

if n == 1:
    pattern = r'[-]?\d+(?:\.\d*)?'
    numbers = [float(item) for item in re.findall(pattern, x)]
    if len(numbers) == 0:
        print(u'В строке нет вещественных чисел!')
    else:
        print(u'Максимальное число: ', max(numbers))

#Найти в строке минимальное из имеющихся в ней рациональных чисел

if n == 2:
    pattern = r'[-]?\d+(?:\.\d*)?'
    numbers2 = [float(item) for item in re.findall(pattern, x)]
    if len(numbers2) == 0:
        print(u'В строке нет рациональных чисел!')
    else:
        print(u'Минимальное число: ', min(numbers2))

#Найти в строке наибольшее количество идущих подряд цифр

if n == 3:
    numbers3 = re.findall(r'\d+', x)
    maxlen = 0
    for i in numbers3:
        if len(i) > maxlen:
            maxlen = len(i)
    print(u'Наибольшее количество идущих подряд цифр: ', maxlen)
