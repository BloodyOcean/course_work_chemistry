import lorem
from lorem.text import TextLorem
from generators import Generator
import random


class EmailGenerator(Generator):
    def __init__(self, *, domains=None):
        if domains is None:
            domains = ['lpnu.ua', 'gmail.com', 'ukr.net']
        self.lorem = TextLorem(wsep='.', srange=[2, 3])
        self.domains = domains

    def next(self) -> str:
        return '\'' + self.lorem.sentence() + '@' + random.choice(self.domains) + '\''
