from generators import Generator
import random
import re


# an example : 2017-07-28 18:34:55.830
class DatetimeGenerator(Generator):
    def __init__(self, *, start: str, end: str):
        self.start_values = [int(x) for x in re.split('[- :.]', start)]
        self.end_values = [int(x) for x in re.split('[- :.]', end)]
        self.separators = [char for char in start if not char.isnumeric()]
        self.sizes = [len(x) for x in re.split('[- :.]', start)]

    def next(self) -> str:
        result = ''
        for i in range(len(self.start_values)):
            next_value = str(random.randint(self.start_values[i], self.end_values[i]))
            if len(next_value) < self.sizes[i]:
                next_value = next_value.rjust(self.sizes[i], '0')
            result += next_value
            if i != len(self.separators):
                result += self.separators[i]
        return '\'' + result + '\''


