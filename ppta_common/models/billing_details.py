from mongoengine import EmbeddedDocument, StringField, DictField


class BillingDetails(EmbeddedDocument):
    email = StringField(default="", required=True)
    name = StringField(default="", required=False)
    phone = StringField(default="", required=False)
    tax_id = StringField(default="", required=False)
    address = DictField(required=False)