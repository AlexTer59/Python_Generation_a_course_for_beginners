# Дано натуральное число n. Напишите программу, которая выводит таблицу
# умножения на n.
#
# Формат входных данных
# На вход программе подается натуральное число.
#
# Формат выходных данных
# Программа должна вывести таблицу умножения на введенное число.
#
# Примечание. В качестве знака умножения используйте английскую букву x.


num = int(input())
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)
