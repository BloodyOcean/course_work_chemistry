from generators import Generator


class TemplatedGenerator(Generator):
    def __init__(self, parts, brackets=True):
        self.parts = parts
        self.brackets = brackets


    def next(self) -> str:
        result = ''
        for part, gen in self.parts:
            result += part + gen.next()
        return f'\'{result}\'' if self.brackets else result


