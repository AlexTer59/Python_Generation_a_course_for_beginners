# Напишите функцию is_palindrome(text), которая принимает в качестве
# аргумента строку text и возвращает значение True если указанный текст
# является палиндромом и False в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих
# направлениях
#
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми,
# а также игнорируйте пробелы, а также символы , . ! ? -.


def is_valid_password(password):
    counter = 0
    password = password.split(':')
    if len(password) != 3:
        return False

    if password[0] != password[0][::-1]:
        return False

    for i in range(1, int(password[1]) + 1):
        if int(password[1]) % i == 0:
            counter += 1
    if counter != 2:
        return False
    if int(password[2]) % 2 != 0:
        return False
    return True


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
