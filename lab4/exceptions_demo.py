# Шаг 1: Минимум 2 функции без обработки исключений
def divide(a, b):  # Функция выбрасывает исключение при b == 0
    # Деление на ноль выбросит исключение ZeroDivisionError
    return a / b

def get_list_element(lst, index):  # Функция выбрасывает исключение при неверном индексе
    # Неверный индекс выбросит исключение IndexError
    return lst[index]


# Шаг 2: Функция с обработчиком общего типа (Exception), без finally
def safe_divide(a, b):
    try:
        return a / b
    except Exception as e:  # Общий обработчик
        print(f"Ошибка при делении: {e}")
        return None


# Шаг 3: Функция с обработчиком общего типа (Exception), с finally
def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None
    finally:
        print("Завершаем работу с файлом.")


# Шаг 4: Три функции с несколькими типами исключений
def calculate_square_root(value):
    try:
        if value < 0:
            raise ValueError("Корень из отрицательного числа невозможен.")
        return value ** 0.5
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    finally:
        print("Завершение работы функции calculate_square_root.")

def parse_number(string):
    try:
        return int(string)
    except ValueError as ve:
        print(f"ValueError: Невозможно преобразовать '{string}' в число.")
    except TypeError as te:
        print(f"TypeError: Некорректный тип данных '{string}'.")

def access_dict_key(data, key):
    try:
        return data[key]
    except KeyError as ke:
        print(f"KeyError: Ключ '{key}' не найден.")
    except TypeError as te:
        print(f"TypeError: Некорректный тип данных: {data}")


# Шаг 5: Функция с генерацией и обработкой всех исключений
def process_input(value):
    try:
        if not isinstance(value, int):
            raise TypeError("Ожидается целое число.")
        if value < 0:
            raise ValueError("Число должно быть положительным.")
        return value * 2
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    finally:
        print("Функция завершена.")


# Шаг 6: Пользовательские исключения
class NegativeNumberError(Exception):
    pass

class EmptyInputError(Exception):
    pass

class InvalidOperationError(Exception):
    pass


# Шаг 7: Функция с пользовательским исключением
def check_positive_number(value):
    try:
        if value < 0:
            raise NegativeNumberError("Число не должно быть отрицательным.")
    except NegativeNumberError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Функция завершена.")


# Шаг 8: Примеры функций, демонстрирующих работу исключений
def demo_zero_division():
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

def demo_index_error():
    try:
        lst = [1, 2, 3]
        return lst[5]
    except IndexError as e:
        print(f"IndexError: {e}")

def demo_type_error():
    try:
        return "5" + 10
    except TypeError as e:
        print(f"TypeError: {e}")
