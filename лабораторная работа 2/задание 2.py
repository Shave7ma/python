word_list = input(u'Введите одну строку со словами: ').split()
list_of_values = []
for i in range(0, len(word_list)):
    list_of_values.insert(i, 0)
    for j in range(len(list_of_values) - 2, -1, -1):
        if word_list[j] == word_list[i]:
            list_of_values[i] = list_of_values[j] + 1
            break

print(u'Вот, сколько раз до этого встречалось каждое слово:', end = ' ')
for i in range (0, len(list_of_values)):
    print(list_of_values[i], end = ' ')
