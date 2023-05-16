from models.models import OrderItem

class OrderItemDeformationInterface:
    def spoil(self, item:OrderItem) -> OrderItem:
        raise NotImplementedError()

class OrderItemDeformation(OrderItemDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, item:OrderItem) -> OrderItem:
        # There's no fields which could be spoilt
        return item