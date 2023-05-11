# На вход программе подается одна строка с буквами русского языка. Напишите
# программу, которая определяет количество гласных и согласных букв.
#
# Формат входных данных
# На вход программе подается одна строка.
#
# Формат выходных данных
# Программа должна вывести количество гласных и согласных букв.
#
# Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е)
# и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).


str = input().lower()
counter_glas = 0
counter_sogl = 0
for i in range(len(str)):
    if str[i] in ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']:
        counter_glas += 1
    if str[i] in ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
                  'щ']:
        counter_sogl += 1

print('Количество гласных букв равно', counter_glas)
print('Количество согласных букв равно', counter_sogl)
