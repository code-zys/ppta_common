from mongoengine import StringField, FloatField, EmbeddedDocument
from .base_document import BaseDocument


class PaymentIntentEmbeddedDocument(EmbeddedDocument):
    """
    PaymentIntent model
    """
    payment_intent_id = StringField(
        required=True, description="The id of the payment_intent provided by stripe"
    )
    amount = FloatField(required=True)


class PaymentIntent(BaseDocument):
    payment_intent_id = StringField(
        required=True, description="The id of the payment_intent provided by stripe"
    )
    amount = FloatField(required=True)
    refunded_amount = FloatField(
        required=True,
        default=0,
        description="Amount of thy payment intent already used for refund"
    )