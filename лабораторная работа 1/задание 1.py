print(u'Введите число: ')
x = input()
while x.isdigit() == False:
    print(u'Это не число, пробуйте еще!')
    x = input()
x = int(x)

#Найти сумму простых делителей числа

def is_prime(n):
    for i in range (2, n//2):
        if n % i == 0:
            return False
    return True

def sum_of_prime_divs(x):
    s = 0
    for i in range (2, x//2):
        if x % i == 0 and is_prime(i):
            s += i
    return s

print(u'Сумма простых делителей числа: ', sum_of_prime_divs(x))

#Найти количество нечетных цифр числа, больших 3

def amount_of_odd_numbers(x):
    c = 0
    clone = x
    while clone != 0:
        if clone % 10 > 3 and clone % 10 % 2 != 0:
            c += 1
        clone //= 10
    return c

print (u'Количество нечетных цифр числа, больших 3: ', amount_of_odd_numbers(x))

#Найти произведение таких делителей числа, сумма цифр которых меньше, чем сумма цифр исходного числа

def sum_of_numbers(n):
    s1 = 0
    clone1 = n
    while clone1 != 0:
        s1 += clone1 % 10
        clone1 //= 10
    return s1

def composition_of_divs(x):
    comp = 1
    for i in range (2, x//2):
        if x % i == 0 and sum_of_numbers(x) > sum_of_numbers(i):
            comp *= i
    return comp

print (u'Произведение делителей числа, сумма цифр которых меньше чем сумма цифр исходного числа: ', composition_of_divs(x))
