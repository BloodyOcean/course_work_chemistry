from models.models import Customer
from deformation import deformate_string


class CustomerDeformationInterface:
    def spoil(self, customer:Customer) -> Customer:
        raise NotImplementedError()

class CustomerDeformation(CustomerDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, customer:Customer) -> Customer:
        customer.first_name = deformate_string(customer.first_name, self.probability)
        customer.last_name = deformate_string(customer.last_name, self.probability)
        customer.email = deformate_string(customer.email, self.probability)
        customer.phone_number = deformate_string(customer.phone_number, self.probability)
        customer.address = deformate_string(customer.address, self.probability)
        customer.city = deformate_string(customer.city, self.probability)
        customer.state = deformate_string(customer.state, self.probability)
        customer.zip_code = deformate_string(customer.zip_code, self.probability)
        return customer
