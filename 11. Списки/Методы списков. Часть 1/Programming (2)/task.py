# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Формат выходных данных
# Программа должна вывести указанный список.
#
# Примечание. Последний элемент списка состоит из 26 символов z.


alph = []
for i in range(1, 27):
    char = chr(i + 96)
    char = char * i
    alph.append(char)
print(alph)
