from mongoengine import  StringField, FloatField, IntField, BooleanField, EmbeddedDocumentField,ReferenceField
from ..enums.currency_type_enum import EnumCurencyType
from .card import Card
from ..enums.card_type_enum import EnumCardType
from .customer import Customer
from .payment_detail import PaymentDetails
from .base_document import BaseDocument
from .billing_details import BillingDetails
from .coaching import Coaching
from .company import Company

class Payment(BaseDocument):
    amount=IntField(required=True)
    currency= StringField(choices=[e.value for e in EnumCurencyType], required=True)
    received_date = IntField( required=True)
    is_successful = BooleanField( required=False)
    payment_method_details = EmbeddedDocumentField(PaymentDetails, required=False, description="Details du payment", default=None)#TODO: To be removed
    customer = EmbeddedDocumentField(Customer, required=False, description="The card of the payment", default=None)#TODO: To be removed
    card = EmbeddedDocumentField(Card, description="The card of the payment", required=False)#TODO: To be removed
    type = StringField(choices=[e.value for e in EnumCardType], required=False)#TODO: To be removed
    coach_percentage = FloatField(required=False) #TODO: To be removed
    invoice_link = StringField(required=False)
    payment_method_id = StringField(required=False)
    company = ReferenceField(Company, required=True)
    stripe_customer_id = StringField(required=False)
    transaction_id= StringField(required=False)
    billing_details = EmbeddedDocumentField(BillingDetails, required=True)
    coaching_id = StringField(required=False, description="The coaching of the payment" )
    
    meta = {
        "collection": "coaching_payments",
    }