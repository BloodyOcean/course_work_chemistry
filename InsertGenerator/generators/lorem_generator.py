import lorem
from lorem.text import TextLorem
from generators import Generator


class LoremGenerator(Generator):
    def __init__(self, *, min_words=1, max_words=11):
        self.min_words = min_words
        self.max_words = max_words
        self.lorem = TextLorem(srange=(self.min_words, self.max_words))

    def next(self) -> str:
        return '\'' + lorem.sentence() + '\''
