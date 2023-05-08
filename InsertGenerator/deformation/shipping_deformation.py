from models.models import Shipping
from deformation import deformate_string


class ShippingDeformationInterface:
    def spoil(self, shipping:Shipping) -> Shipping:
        raise NotImplementedError()

class ShippingDeformation(ShippingDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, shipping: Shipping) -> Shipping:
        shipping.carrier = deformate_string(shipping.carrier, self.probability)
        shipping.receiver = deformate_string(shipping.receiver ,self.probability)
        shipping.tracking_number = deformate_string(shipping.tracking_number ,self.probability)
        shipping.shipping_address = deformate_string(shipping.shipping_address ,self.probability)
        shipping.shipping_city =  deformate_string(shipping.shipping_city ,self.probability)
        shipping.shipping_state =  deformate_string(shipping.shipping_state ,self.probability)
        shipping.shipping_zip =  deformate_string(shipping.shipping_zip ,self.probability)
        return shipping