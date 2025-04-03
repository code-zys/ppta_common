from mongoengine import  StringField, FloatField, IntField, BooleanField, ReferenceField
from ..enums.currency_type_enum import EnumCurencyType
from card import Card
from ..enums.card_type_enum import EnumCardType
from .customer import Customer
from .payment_detail import PaymentDetails
from .base_document import BaseDocument

class Payment(BaseDocument):
    amount=FloatField(required=True)
    currency= StringField(choices=[e.value for e in EnumCurencyType], required=True)
    receivedDate = IntField( required=True)
    isSuccessful = BooleanField( required=False)
    billing_details=ReferenceField(PaymentDetails, description="The details of the payment", required=False), 
    customer=ReferenceField(Customer, description="The card of the payment", required=False), 
    card=ReferenceField(Card, description="The card of the payment", required=False), 
    type=StringField(choices=[e.value for e in EnumCardType], required=False)
    coach_percentage = FloatField(required=False)
    invoice_link = StringField(required=False)