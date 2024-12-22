from functions import *

if __name__ == "__main__":
    print(greet())  # Пример вызова функции без параметров
    print(square(4))  # Пример вызова функции с параметром
    print(power(3))  # Пример вызова функции со значением по умолчанию
    print(multiply(3, 5))  # Функция с заданным типом параметров
    print(sum_all(1, 2, 3, 4))  # Функция с args
    print(print_info(name="Alice", age=25))  # Функция с kwargs
    print(call_inner_function())  # Вызов функции, которая вызывает другую функцию
    
    # Вызов функции, принимающей другую функцию
    print(apply_function(square, 5))
    print(compare_values(lambda x, y: x > y, 10, 5))
    
    # Локальная функция
    print(outer_function_1())
    print(outer_function_2(7))
    
    # Лямбда-выражения
    print(no_param())
    print(add(10, 20))
    print(use_lambda(lambda x, y: x * y, 5, 6))
    
    # Замыкания
    inc = closure_example_2()
    print(inc())
    print(inc())
    
    doubler = closure_example_3(2)
    print(doubler(5))