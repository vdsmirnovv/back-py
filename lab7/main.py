# main.py
from string_utils import *

def main():
    # Задание 1
    formatted = format_string("World", 10 + 5, custom_function(5))
    print(f"Task 1: {formatted}\n")
    
    # Задание 2
    repeated = repeat_strings("Hello", "World", 3)
    print(f"Task 2:\n{repeated}\n")
    
    # Задание 3
    count = count_substring("Hello World! Hello Again!", "hello")
    print(f"Task 3: Substring count is {count}\n")
    
    # Задание 4
    substring = substring_between_indices("This is a test string", 5, 10)
    print(f"Task 4: Substring is '{substring}'\n")
    
    # Задание 5
    latin_words, count = find_latin_letters("Привет Hello мир World", "Это text")
    print(f"Task 5: Latin words are {latin_words}, count is {count}\n")
    
    # Задание 6
    palindrome_check = is_palindrome("A man a plan a canal Panama")
    print(f"Task 6: Is palindrome? {palindrome_check}\n")
    
    # Задание 7
    length = normalize_whitespace("  This   is  a test   ")
    print(f"Task 7: Normalized string length is {length}\n")
    
    # Задание 8
    replaced = replace_sentence_endings("Hello world. How are you? I am fine!")
    print(f"Task 8:\n{replaced}\n")
    
    # Задание 9
    reversed_words = reverse_words("Hello World")
    print(f"Task 9.1: {reversed_words}")
    
    alternate_caps = capitalize_alternate("this is a test string")
    print(f"Task 9.2: {alternate_caps}")
    
    digit_count = count_digits("This string has 12345 digits")
    print(f"Task 9.3: {digit_count}")
    
if __name__ == "__main__":
    main()
