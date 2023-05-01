import random
import string
from generators import Generator

DEFAULT_DOMAINS = ['lpnu.ua', 'gmail.com', 'ukr.net']


class EmailGenerator(Generator):

    def __init__(self, *, domains=None):
        self.domains = domains or DEFAULT_DOMAINS

    def next(self) -> str:
        username = ''.join(random.choices(string.ascii_lowercase, k=10))
        domain = random.choice(self.domains)
        return f'\'{username}@{domain}\''
