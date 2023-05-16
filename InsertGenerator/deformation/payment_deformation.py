from models.models import Payment
from deformation import deformate_string


class PaymentDeformationInterface:
    def spoil(self, payment:Payment) -> Payment:
        raise NotImplementedError()


class PaymentDeformation(PaymentDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, payment:Payment) -> Payment:
        payment.card_number = deformate_string(payment.card_number, self.probability)
        payment.card_holder = deformate_string(payment.card_holder, self.probability)
        return payment
