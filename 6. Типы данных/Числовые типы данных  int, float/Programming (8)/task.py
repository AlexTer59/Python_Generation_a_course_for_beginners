# Напишите программу, которая упорядочивает три числа от большего к меньшему.
#
# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных
# от большего к меньшему.


num1, num2, num3 = int(input()), int(input()), int(input())
min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
if min_num < num1 < max_num:
    mid_num = num1
elif min_num < num2 < max_num:
    mid_num = num2
elif min_num < num3 < max_num:
    mid_num = num3
else:
    mid_num = max_num
print(max_num)
print(mid_num)
print(min_num)
