from models.models import Packaging
from deformation import deformate_string


class PackagingDeformationInterface:
    def spoil(self, packaging:Packaging) -> Packaging:
        raise NotImplementedError()

class PackagingDeformation(PackagingDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, packaging: Packaging) -> Packaging:
        packaging.name = deformate_string(packaging.name, self.probability)
        packaging.description = deformate_string(packaging.description, self.probability)
        return packaging