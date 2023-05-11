# Дано натуральное число. Напишите программу, которая вычисляет:
#
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке.


n = int(input())
n_l_d = n % 10
count_last_digit = 0
count_3 = 0
count_chet = 0
count_more_5 = 0
proizv_more_7 = 1
count_5_0 = 0
while n != 0:
    last_digit = n % 10
    if last_digit == 3:
        count_3 += 1
    if last_digit % 2 == 0:
        count_chet += 1
    if last_digit == n_l_d:
        count_last_digit += 1
    if last_digit > 5:
        count_more_5 += last_digit
    if last_digit > 7:
        proizv_more_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        count_5_0 += 1
    n //= 10
print(count_3)
print(count_last_digit)
print(count_chet)
print(count_more_5)
print(proizv_more_7)
print(count_5_0)
