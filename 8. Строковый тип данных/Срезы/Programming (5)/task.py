# На вход программе подается одна строка. Напишите программу, которая выводит:
#
# общее количество символов в строке;
# исходную строку, повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.
# Формат входных данных
# На вход программе подается одна строка, длина которой больше 3 символов.
#
# Формат выходных данных
# Программа должна вывести данные в соответствии с условием. Каждое значение
# выводится на отдельной строке.


str = input()
print(len(str))
print(str + str + str)
print(str[0])
print(str[:3])
print(str[-3:])
print(str[::-1])
print(str[1:-1])
