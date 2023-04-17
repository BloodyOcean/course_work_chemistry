from generators import Generator


class DefaultGenerator(Generator):
    def __init__(self):
        pass

    def next(self) -> str:
        return 'DEFAULT'