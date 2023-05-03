import random


def deformate_string(value: str, probability: float):
    if random.random() > probability:
        return value
    prefix_spaces = random.randint(0, 3) * ' '
    suffix_spaces = random.randint(0, 3) * ' '
    return f'{prefix_spaces}{value}{suffix_spaces}'