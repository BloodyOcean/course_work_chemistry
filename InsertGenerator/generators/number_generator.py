import random
from generators import Generator


class NumberGenerator(Generator):
    def __init__(self, *, start=0, end=1000000, queue_mode=False, brackets=False, stay_for=1):
        self.start = start
        self.stay_for = stay_for
        self.end = end
        self.brackets = brackets
        self.queue_counter = start if queue_mode else None
        self.stay_counter = 0

    def next(self) -> str:
        if self.queue_counter is not None:
            val = self.queue_counter
            if val == self.end:
                self.queue_counter = self.start
            if self.stay_counter == self.stay_for - 1:
                self.queue_counter += 1
                self.stay_counter = 0
            else:
                self.stay_counter += 1
            return str(val)

        return str(random.randint(self.start, self.end))


class FloatGenerator(Generator):
    def __init__(self, start, end, precision=4, round_to=0.0005, brackets=False):
        self.start = start
        self.end = end
        self.brackets = brackets
        self.precision = precision

    def next(self) -> str:
        if self.brackets:
            return '\'' + str(round(random.uniform(self.start, self.end), self.precision - 1)) + '0' + '\''
        return str(round(random.uniform(self.start, self.end), self.precision - 1)) + '0'
