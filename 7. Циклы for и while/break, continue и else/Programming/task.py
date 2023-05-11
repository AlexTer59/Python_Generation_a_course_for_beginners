# На вход программе подается число n>1. Напишите программу, которая
# выводит его наименьший отличный от 1 делитель.
#
# Формат входных данных
# На вход программе подается одно натуральное число n.
#
# Формат выходных данных
# Программа должна вывести наименьший делитель отличный от 1.
#
# Примечание. Используйте оператор break при обнаружении делителя.


num = int(input())
for i in range(2, num + 1):
    if num % i == 0:
        break
print(i)
