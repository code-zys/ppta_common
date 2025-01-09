from mongoengine import EmbeddedDocument, StringField

class PaymentDetails(EmbeddedDocument):
    ownerName = StringField(default="", required=True)
    bankName = StringField(default="", required=True)
    accountNumber = StringField(default="", required=True)