import string
from generators import Generator
import random

class HashGenerator(Generator):
    def __init__(self, length=32, brackets=False):
        self.length = length
        self.brackets = brackets

    def next(self) -> str:
        result = ''
        for i in range(self.length):
            give_char = bool(random.randint(0, 1))
            if give_char:
                result += random.choice(string.ascii_letters)
            else:
                result += str(random.randint(0, 9))

        if self.brackets:
            return '\'' + result + '\''
        return result

