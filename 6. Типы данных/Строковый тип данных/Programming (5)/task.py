# Напишите программу, которая считывает одну строку, после чего выводит
# «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.
#
# Формат входных данных
# На вход программе подается одна строка.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.


s1 = input()
if 'синий' in s1:
    print('YES')
else:
    print('NO')