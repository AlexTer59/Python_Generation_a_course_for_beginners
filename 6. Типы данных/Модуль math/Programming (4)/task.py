# Напишите программу, вычисляющую значение ⌈x⌉+⌊x⌋ по заданному вещественному
# числу x.
#
# Формат входных данных
# На вход программе подается одно вещественное число x.
#
# Формат выходных данных
# Программа должна вывести одно число – значение указанного выражения.
#
# Примечание. ⌈x⌉ – потолок числа, ⌊x⌋ – пол числа.


from math import *

x = float(input())
print(floor(x) + ceil(x))
