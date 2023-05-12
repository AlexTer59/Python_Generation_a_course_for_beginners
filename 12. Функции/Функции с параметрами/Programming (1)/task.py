# Напишите функцию print_fio(name, surname, patronymic), которая принимает
# три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.
#
# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь
# верхний регистр.


def print_fio(name, surname, patronymic):
    FIO = []
    FIO.append(surname[:1])
    FIO.append(name[:1])
    FIO.append(patronymic[:1])
    print(''.join(FIO).upper())


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
