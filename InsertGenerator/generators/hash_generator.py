import string
from generators import Generator
import secrets

class HashGenerator(Generator):

    def __init__(self, length=32):
        self.length = length


    def next(self) -> str:
        alphabet = string.ascii_letters + string.digits
        hash = ''.join(secrets.choice(alphabet) for i in range(self.length))
        return hash

