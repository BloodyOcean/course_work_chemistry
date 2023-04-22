from generators import Generator


class NullGenerator(Generator):
    def __init__(self):
        pass

    def next(self) -> str:
        return 'NULL'

