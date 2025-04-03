from mongoengine import StringField, IntField
from .base_document import BaseDocument

class Card(BaseDocument):
    country = StringField(required=False)
    last4 = StringField(required=False)
    paymentMethodId = StringField(required=True)
    exp_month = IntField(required=True)
    exp_year  = IntField(required=True)