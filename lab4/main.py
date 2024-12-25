from exceptions_demo import *

if __name__ == "__main__":
    # Шаг 9: Функция, вызывающая все остальные
    def test_all_functions():
        print("Тестируем функции из шага 1...")
        try:
            print(divide(10, 2))
            print(get_list_element([1, 2, 3], 1))
        except Exception as e:
            print(f"Ошибка: {e}")
        
        print("\nТестируем функции из шага 2...")
        print(safe_divide(10, 0))
        
        print("\nТестируем функции из шага 3...")
        print(safe_read_file("nonexistent.txt"))
        
        print("\nТестируем функции из шага 4...")
        calculate_square_root(-4)
        parse_number("abc")
        access_dict_key({"key": "value"}, "nonexistent_key")
        
        print("\nТестируем функции из шага 5...")
        process_input("string")
        process_input(-10)
        
        print("\nТестируем пользовательские исключения...")
        check_positive_number(-5)
        
        print("\nДемонстрация исключений...")
        demo_zero_division()
        demo_index_error()
        demo_type_error()
    
    test_all_functions()
