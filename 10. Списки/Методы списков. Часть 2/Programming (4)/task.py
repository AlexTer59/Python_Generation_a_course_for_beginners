# На вход программе подается строка текста, содержащая целые числа.
# Из данной строки формируется список чисел. Напишите программу, которая сортирует
# и выводит данный список сначала по возрастанию, а затем по убыванию.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести две строки текста в соответствии с условием задачи.


s_num = input()
l_num = s_num.split(' ')
for i in range(len(l_num)):
    l_num[i] = int(l_num[i])
l_num.sort()
print(*l_num)
l_num.sort(reverse=True)
print(*l_num)
