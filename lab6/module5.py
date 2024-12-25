import random

def random_numbers():
    return [random.randint(1, 100) for _ in range(10)]

def random_choice():
    return random.choice(['A', 'B', 'C', 'D'])