from generators import Generator
import names


class NameGenerator(Generator):
    def __init__(self, *, firstname=True, lastname=True):
        self.fn = firstname
        self.ln = lastname

    def next(self) -> str:
        result = None

        if self.fn == self.ln:
            result = names.get_full_name()
        elif self.ln:
            result = names.get_last_name()
        else:
            result = names.get_first_name()

        return f'\'{result}\''
