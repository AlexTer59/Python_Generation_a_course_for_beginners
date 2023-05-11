# Напишите программу, которая принимает три положительных числа
# и определяет вид треугольника, длины сторон которого равны введенным числам.
#
# Формат входных данных
# На вход программе подаются три числа – длины сторон существующего треугольника.
#
# Формат выходных данных
# Программа должна вывести на экран текст – вид треугольника
# («Равносторонний», «Равнобедренный» или «Разносторонний»).


a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')
