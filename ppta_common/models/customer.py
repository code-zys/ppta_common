from mongoengine import EmailField, StringField,IntField
from .base_document import BaseDocument

class Customer(BaseDocument):
    email = EmailField(required=False)
    name = StringField(required=True)
    phone =StringField(required=False)
    country = StringField(required=False)
    city = StringField(required=False)
    postal_code = IntField(required=False)