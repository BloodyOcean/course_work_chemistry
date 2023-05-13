from models.models import Manufacturer
from deformation import deformate_string


class ManufacturerDeformationInterface:
    def spoil(self, manufacturer:Manufacturer) -> Manufacturer:
        raise NotImplementedError()

class ManufacturerDeformation(ManufacturerDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, manufacturer: Manufacturer) -> Manufacturer:
        manufacturer.name = deformate_string(manufacturer.name, self.probability)
        manufacturer.description = deformate_string(manufacturer.description, self.probability)
        manufacturer.contact_person = deformate_string(manufacturer.contact_person, self.probability)
        manufacturer.email = deformate_string(manufacturer.email, self.probability)
        return manufacturer