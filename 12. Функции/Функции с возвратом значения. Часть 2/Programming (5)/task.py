# Напишите функцию is_palindrome(text), которая принимает в качестве
# аргумента строку text и возвращает значение True если указанный текст
# является палиндромом и False в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих
# направлениях
#
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми,
# а также игнорируйте пробелы, а также символы , . ! ? -.


def is_palindrome(text):
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace('-', '')
    text = text.replace(' ', '')
    text = text.lower()
    if text[:] == text[::-1]:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
