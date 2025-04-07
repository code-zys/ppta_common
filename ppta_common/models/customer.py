from mongoengine import EmailField, StringField,IntField, EmbeddedDocument

class Customer(EmbeddedDocument):
    email = EmailField(required=False)
    name = StringField(required=True)
    phone =StringField(required=False)
    country = StringField(required=False)
    city = StringField(required=False)
    postal_code = IntField(required=False)