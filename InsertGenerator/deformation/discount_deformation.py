from models.models import Discount
from deformation import deformate_string


class DiscountDeformationInterface:
    def spoil(self, payment:Discount) -> Discount:
        raise NotImplementedError()


class DiscountDeformation(DiscountDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, discount:Discount) -> Discount:
        discount.title = deformate_string(discount.title, self.probability)
        discount.description= deformate_string(discount.description, self.probability)
        return discount
