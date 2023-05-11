# На вход программе подается натуральное число n и n строк, а затем
# число k. Напишите программу, которая выводит k-ую букву из введенных
# строк на одной строке без пробелов.
#
# Формат входных данных
# На вход программе подается натуральное число n,  далее n строк, каждая на
# отдельной строке. В конце вводится натуральное число k – номер буквы
# (нумерация начинается с единицы).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если некоторые строки слишком короткие, и в них нет символа
# с заданным номером, то такие строки при выводе нужно игнорировать.


n = int(input())
list = []
str_ready = ''
for i in range(n):
    str = input()
    list.append(str)
n_char = int(input())
for k in range(n):
    if (len(list[k])) >= n_char:
        str_ready += list[k][n_char - 1]
print(str_ready)
