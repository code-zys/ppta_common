from mongoengine import StringField, IntField, EmbeddedDocument

class Card(EmbeddedDocument):
    country = StringField(required=False)
    last4 = StringField(required=False)
    paymentMethodId = StringField(required=True)
    exp_month = IntField(required=True)
    exp_year  = IntField(required=True)