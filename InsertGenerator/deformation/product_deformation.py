from models.models import Product
from deformation import deformate_string


class ProductDeformationInterface:
    def spoil(self, product:Product) -> Product:
        raise NotImplementedError()

class ProductDeformation(ProductDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, product: Product) -> Product:
        product.name = deformate_string(product.name, self.probability)
        product.description = deformate_string(product.description, self.probability)
        return product