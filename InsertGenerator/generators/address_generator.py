from faker import Faker
from generators import Generator

class AddressGenerator(Generator):

    def __init__(self) -> None:
        self.faker = Faker()


    def next(self):
        address = self.faker.street_address()
        return f'\'{address}\''
