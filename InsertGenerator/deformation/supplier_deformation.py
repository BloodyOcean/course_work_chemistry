from models.models import Supplier
from deformation import deformate_string


class SupplierDeformationInterface:
    def spoil(self, supplier:Supplier) -> Supplier:
        raise NotImplementedError()

class SupplierDeformation(SupplierDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, supplier:Supplier) -> Supplier:
        supplier.name = deformate_string(supplier.name, self.probability)
        supplier.phone_number = deformate_string(supplier.phone_number, self.probability)
        supplier.contact_name = deformate_string(supplier.contact_name, self.probability)
        supplier.email = deformate_string(supplier.email, self.probability)
        return supplier