# Шаг 1. Функция переворачивает список.
def reverse_list(input_list):
    """Возвращает перевёрнутый список."""
    return input_list[::-1]

# Шаг 2. Функция изменяет список.
def modify_list(input_list):
    """Увеличивает каждый элемент списка на 1."""
    return [x + 1 for x in input_list]

# Шаг 3. Функция сравнивает списки.
def compare_lists(*lists):
    """Сравнивает переданные списки на равенство."""
    return all(lists[0] == lst for lst in lists[1:])

# Шаг 4. Функция выбирает диапазон значений из списка.
def slice_list(input_list, start=0, end=None, step=1):
    """
    Возвращает подсписок с заданным диапазоном.
    :param start: Начало диапазона (по умолчанию 0).
    :param end: Конец диапазона (по умолчанию - до конца).
    :param step: Шаг (по умолчанию 1).
    """
    if end is None:
        end = len(input_list)
    return input_list[start:end:step]

# Шаг 5. Функция создаёт список на основе параметров.
def create_list(length, value):
    """Создаёт список из заданной длины и значения."""
    return [value] * length

# Шаг 6. Функция вставляет элемент в список.
def insert_into_list(input_list, position, value):
    """Вставляет значение в список на указанную позицию."""
    input_list.insert(position, value)
    return input_list

# Шаг 7. Функция объединяет и сортирует списки.
def merge_and_sort_lists(*lists, reverse=False):
    """Объединяет списки и сортирует их."""
    combined = sum(lists, [])
    return sorted(combined, reverse=reverse)

# Шаг 8. Функция создаёт списки и анализирует их длину.
def analyze_list_length():
    """Создаёт список и проверяет его длину на чётность."""
    import random
    while True:
        lst = [random.randint(1, 10) for _ in range(random.randint(5, 15))]
        if len(lst) % 2 == 1:
            center = lst[len(lst) // 2]
            return center, lst.count(center)

# Шаг 9. Функция модифицирует список с учётом порога.
def modify_list_with_threshold(main_list, *lists, threshold):
    """Прибавляет списки и обрезает до порога."""
    main_list.extend(sum(lists, []))
    if len(main_list) > threshold:
        main_list = main_list[:threshold]
    return main_list

# Шаг 10. Функции сортировки списка с использованием map.
def sort_by_length(input_list):
    """Сортирует строки по длине."""
    return sorted(input_list, key=len)

def square_sort(input_list):
    """Сортирует числа по их квадрату."""
    return sorted(input_list, key=lambda x: x**2)

def reverse_sort(input_list):
    """Сортирует в обратном порядке."""
    return sorted(input_list, reverse=True)

# Шаг 11. Функция извлекает минимальный элемент.
def extract_minimum(input_list):
    """Извлекает минимальный элемент из списка."""
    if not input_list:
        return None
    min_value = min(input_list)
    input_list.remove(min_value)
    return min_value

# Шаг 12. Функции с кортежами.
def sum_tuples(*tuples):
    """Суммирует все элементы кортежей."""
    return tuple(sum(x) for x in zip(*tuples))

def multiply_tuples(t1, t2):
    """Перемножает элементы двух кортежей."""
    return tuple(x * y for x, y in zip(t1, t2))

# Шаг 13. Функция создаёт кортеж типов данных.
def types_in_tuple(input_tuple):
    """Возвращает кортеж типов данных элементов входного кортежа."""
    return tuple(type(x) for x in input_tuple)

# Шаг 14. Функция проверяет наличие элемента в кортеже.
def check_element_in_tuple(input_tuple, element):
    """Проверяет наличие элемента в кортеже."""
    return element in input_tuple

# Шаг 15. Функция создаёт двумерный список.
def create_2d_list(*lists):
    """Формирует двумерный список."""
    return [list(x) for x in zip(*lists)]

# Шаг 16. Функции с операциями над словарями.
def dict_keys_sum(dictionary):
    """Возвращает сумму всех ключей (если ключи - числа)."""
    return sum(k for k in dictionary if isinstance(k, (int, float)))

def dict_values_product(dictionary):
    """Возвращает произведение всех значений (если значения - числа)."""
    product = 1
    for v in dictionary.values():
        if isinstance(v, (int, float)):
            product *= v
    return product

def dict_items_stringify(dictionary):
    """Возвращает строку, содержащую все пары ключ-значение."""
    return ', '.join(f"{k}: {v}" for k, v in dictionary.items())

# Шаг 17. Функция ищет ключи в нескольких словарях.
def count_key_in_dicts(key, *dicts):
    """Считает, в скольких словарях присутствует ключ."""
    return sum(1 for d in dicts if key in d)

# Шаг 18. Функция ищет элемент в глубоко вложенном словаре.
def find_deep_key(dictionary, key):
    """Ищет ключ на самом глубоком уровне вложенности."""
    def recursive_search(d):
        if key in d:
            return d[key]
        for value in d.values():
            if isinstance(value, dict):
                result = recursive_search(value)
                if result is not None:
                    return result
        return None

    return recursive_search(dictionary)

# Шаг 19. Функция вызывает все остальные.
def run_all_functions():
    """Вызывает все функции для демонстрации их работы."""
    print("Шаг 1:", reverse_list([1, 2, 3, 4]))
    print("Шаг 2:", modify_list([1, 2, 3]))
    print("Шаг 3:", compare_lists([1, 2], [1, 2], [1, 2]))
    print("Шаг 4:", slice_list([0, 1, 2, 3, 4, 5], start=1, end=5, step=2))
    print("Шаг 5:", create_list(5, 10))
    print("Шаг 6:", insert_into_list([1, 2, 3], 1, 99))
    print("Шаг 7:", merge_and_sort_lists([3, 2, 1], [6, 5, 4], reverse=True))
    print("Шаг 8:", analyze_list_length())
    print("Шаг 9:", modify_list_with_threshold([1, 2, 3], [4, 5], [6, 7], threshold=5))
    print("Шаг 10:", sort_by_length(["apple", "kiwi", "banana"]))
    print("Шаг 11:", extract_minimum([3, 1, 2]))
    print("Шаг 12:", sum_tuples((1, 2), (3, 4)))
    print("Шаг 13:", types_in_tuple((1, "string", 3.0)))
    print("Шаг 14:", check_element_in_tuple((1, 2, 3), 2))
    print("Шаг 15:", create_2d_list([1, 2], [3, 4]))
    print("Шаг 16:", dict_keys_sum({1: "a", 2: "b"}))
    print("Шаг 17:", count_key_in_dicts("name", {"name": "Alice"}, {"age": 25}))
    print("Шаг 18:", find_deep_key({"level1": {"level2": {"key": "value"}}}, "key"))
