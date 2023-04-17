from generators import Generator
import random


class SpecialGenerator(Generator):
    def __init__(self, *, special_values, brackets=True):
        self.values = special_values
        self.brackets = brackets

    def next(self) -> str:
        if self.brackets:
            return '\'' + str(self.values[random.randint(0, len(self.values) - 1)]) + '\''
        else:
            return str(self.values[random.randint(0, len(self.values) - 1)])
