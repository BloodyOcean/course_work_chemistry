from generators import Generator
import random
import names


class NameGenerator(Generator):
    def __init__(self, *, firstname=True, lastname=True, brackets=False):
        self.fn = firstname
        self.ln = lastname
        self.brackets = brackets

    def next(self) -> str:
        result = None
        if self.fn and self.ln:
            result = names.get_full_name()
        elif self.ln:
            result = names.get_last_name()
        else:
            result = names.get_first_name()

        if self.brackets:
            return '\'' + result + '\''
        return result
