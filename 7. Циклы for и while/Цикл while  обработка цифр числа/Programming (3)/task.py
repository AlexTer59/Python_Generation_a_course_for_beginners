# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке.


num = int(input())
num_d = num
sum = 0
counter = 0
comp = 1
while num != 0:
    last_digit = num % 10
    sum += last_digit
    counter += 1
    comp *= last_digit
    num = num // 10
sr_arf = sum / counter
print(sum)
print(counter)
print(comp)
print(sr_arf)
print(last_digit)
print(last_digit + num_d % 10)
