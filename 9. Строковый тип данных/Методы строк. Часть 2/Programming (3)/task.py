# На вход программе подается строка текста. Напишите программу, которая
# подсчитывает количество цифр в данной строке.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести количество цифр в данной строке.


s = input()
counter = 0
for i in range(len(s)):
    if s[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        counter += 1
print(counter)
