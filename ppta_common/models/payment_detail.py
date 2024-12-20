from mongoengine import EmbeddedDocument, StringField

class PaymentDetails(EmbeddedDocument):
    iban = StringField(required=True, default="")
    bic_swift = StringField(required=False, default="")