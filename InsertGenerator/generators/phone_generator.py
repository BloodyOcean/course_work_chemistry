import random

from generators import Generator


class PhoneGenerator(Generator):
    
    def next(self) -> str:
        area_code = random.randint(100, 999)
        exchange = random.randint(100, 999)
        line_number = random.randint(1000, 9999)
        return f"{area_code}{exchange}{line_number}"
