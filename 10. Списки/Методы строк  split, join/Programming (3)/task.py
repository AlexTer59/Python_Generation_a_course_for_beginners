# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, которая по заданным числам строит столбчатую диаграмму.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.
#
# Формат выходных данных
# Программа должна вывести столбчатую диаграмму.


str = input()
list = str.split(' ')
for i in range(len(list)):
    print(int(list[i]) * '+')
