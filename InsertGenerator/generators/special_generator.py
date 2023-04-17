from generators import Generator
import random


class SpecialGenerator(Generator):
    def __init__(self, *, special_values, brackets=True):
        self.values = special_values
        self.brackets = brackets

    def next(self) -> str:
        value = random.choice(self.values)
        return f'\'{value}\'' if self.brackets else str(value)
