from mongoengine import StringField, FloatField, EmbeddedDocument
from .base_document import BaseDocument
from ..enums.refund_status_enum import EnumRefundStatus


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
    refund_id = StringField(required=True)
    status = StringField(required=True,choices=[status.value for status in EnumRefundStatus])