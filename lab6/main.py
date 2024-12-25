from module1 import module1_func1, module1_func2, module1_func3
from module4 import generate_random_sequence, pick_random
from module6 import math_operations, calculate_area
from dataclasses_module import create_product, update_stock, list_products, customer_purchases

def main():
    print(module1_func1())
    print(module1_func2())
    print(module1_func3())

    print(generate_random_sequence())
    print(pick_random())

    print(math_operations())
    print(calculate_area(5))

    product = create_product("Phone", 700.0, 10)
    print(update_stock(product, 2))

    products = [create_product(f"Item{i}", i * 10, 20) for i in range(5)]
    print(list_products(products))

    print(customer_purchases())

if __name__ == "__main__":
    main()