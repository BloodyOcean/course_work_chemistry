from models.models import ProductCategory
from deformation import deformate_string


class CategoryDeformationInterface:
    def spoil(self, category:ProductCategory) -> ProductCategory:
        raise NotImplementedError()

class CategoryDeformation(CategoryDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, category:ProductCategory) -> ProductCategory:
        category.name = deformate_string(category.name, self.probability)
        return category