from models.models import Order
from deformation import deformate_string


class OrderDeformationInterface:
    def spoil(self, order:Order) -> Order:
        raise NotImplementedError()

class OrderDeformation(OrderDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, order: Order) -> Order:
        order.name = deformate_string(order.name, self.probability)
        return order