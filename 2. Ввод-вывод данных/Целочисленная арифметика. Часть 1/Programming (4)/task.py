# Напишите программу, которая считывает целое число, после чего на экран
# выводится следующее и предыдущее целое число с пояснительным текстом.
#
# Формат входных данных
# На вход программе подаётся целое число.
#
# Формат выходных данных
# Программа должна вывести текст согласно условию задачи.

num = int(input())
print('Следующее за числом', num, 'число:', num + 1)
print('Для числа', num, 'предыдущее число:', num - 1)
