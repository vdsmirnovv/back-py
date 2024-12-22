# Функция без параметров
def greet():
    return "Привет!"

# Функция с параметром
def square(num):
    return num ** 2

# Функция с несколькими параметрами со значениями по умолчанию
def power(base, exp=2):
    return base ** exp

# Функция с несколькими параметрами с заданным типом
def multiply(x: int, y: int) -> int:
    return x * y

# Функция с неопределённым количеством параметров (args)
def sum_all(*args):
    return sum(args)

# Функция с неопределённым количеством параметров (kwargs)
def print_info(**kwargs):
    return ", ".join(f"{key}: {value}" for key, value in kwargs.items())

# Функция, вызывающая другую функцию
def call_inner_function():
    def inner():
        return "Это внутренняя функция"
    return inner()

# Функция, принимающая другую функцию как параметр (3 примера)
def apply_function(func, value):
    return func(value)

def compare_values(func, x, y):
    return func(x, y)

def execute_n_times(func, n):
    for _ in range(n):
        func()

# Функция с локальной функцией (2 примера)
def outer_function_1():
    def local_function():
        return "Локальная функция 1"
    return local_function()

def outer_function_2(x):
    def double():
        return x * 2
    return double()

# Лямбда-выражение без параметров
no_param = lambda: "Лямбда без параметров"

# Лямбда-выражение с параметрами
add = lambda x, y: x + y

# Функция, принимающая лямбду как параметр
def use_lambda(lambda_func, x, y):
    return lambda_func(x, y)

# Функция с замыканием (3 примера)
def closure_example_1(x):
    def inner():
        return x + 1
    return inner

def closure_example_2():
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment

def closure_example_3(multiplier):
    def multiply(x):
        return x * multiplier
    return multiply