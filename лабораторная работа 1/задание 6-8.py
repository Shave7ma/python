import re

print(u'Введите строку: ')
x = input()

#Найти в строке максимальное из имеющихся в ней вещественных чисел

pattern = r'[-]?\d+(?:\.\d*)?'
numbers = [float(item) for item in re.findall(pattern, x)]
if len(numbers) == 0:
    print(u'В строке нет вещественных чисел!')
elif max(numbers).is_integer():
    print(u'Максимальное число: ', int(max(numbers)))
else:
    print(u'Максимальное число: ', max(numbers))

#Найти в строке наибольшее количество идущих подряд цифр

numbers3 = re.findall(r'\d+', x)
maxlen = 0
for i in numbers3:
    if len(i) > maxlen:
        maxlen = len(i)
print(u'Наибольшее количество идущих подряд цифр: ', maxlen)
