# string_utils.py

# Функция для задания 1
def format_string(param1, param2, param3):
    """
    Формирует строку с подстановкой значений:
    - param1: строка
    - param2: результат арифметической операции
    - param3: результат вызова другой функции
    """
    predefined_string = "Hello, {0}! The result of 10 + 5 is {1}, and {2} is the result of a custom function."
    return predefined_string.format(param1, param2, param3)

# Вспомогательная функция для задания 1
def custom_function(value):
    """Возвращает удвоенное значение"""
    return value * 2

# Функция для задания 2
def repeat_strings(string1, string2, repeat_count):
    """
    Формирует строку из повторений комбинации строк.
    Каждое повторение - на новой строке.
    """
    return "\n".join([f"{string1} {string2}" for _ in range(repeat_count)])

# Функция для задания 3
def count_substring(main_string, substring):
    """
    Считает количество вхождений подстроки без учёта регистра.
    """
    return main_string.lower().count(substring.lower())

# Функция для задания 4
def substring_between_indices(string, start_index, end_index):
    """
    Возвращает подстроку между двумя индексами.
    """
    return string[start_index:end_index]

# Функция для задания 5
def find_latin_letters(*strings):
    """
    Находит слова с латинскими буквами среди кириллических.
    """
    result = []
    count = 0
    for string in strings:
        words = string.split()
        for word in words:
            if any(char.isalpha() and not char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" for char in word.lower()):
                result.append(word)
                count += 1
    return result, count

# Функция для задания 6
def is_palindrome(string):
    """
    Определяет, является ли строка палиндромом.
    """
    cleaned_string = "".join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

# Функция для задания 7
def normalize_whitespace(string):
    """
    Удаляет лишние пробелы и возвращает длину строки.
    """
    normalized = " ".join(string.split())
    return len(normalized)

# Функция для задания 8
def replace_sentence_endings(string):
    """
    Заменяет символы окончания предложения на символ переноса строки.
    """
    return string.replace(".", "\n").replace("!", "\n").replace("?", "\n")

# Дополнительные функции для задания 9
def reverse_words(string):
    """Переворачивает каждое слово в строке."""
    return " ".join(word[::-1] for word in string.split())

def capitalize_alternate(string):
    """Делает заглавными каждое второе слово."""
    words = string.split()
    return " ".join(word.upper() if i % 2 == 1 else word for i, word in enumerate(words))

def count_digits(string):
    """Считает количество цифр в строке."""
    return sum(char.isdigit() for char in string)
