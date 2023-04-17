from generators import Generator
import random
import re


# an example : 2017-07-28 18:34:55.830
class TemplatedGenerator(Generator):
    def __init__(self, parts, brackets=True):
        self.parts = parts
        self.brackets = brackets


    def next(self) -> str:
        result = ''
        for part, gen in self.parts:
            result += part + gen.next()
        if self.brackets:
            return '\'' + result + '\''
        return result


