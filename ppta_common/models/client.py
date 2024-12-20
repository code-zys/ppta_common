from mongoengine import StringField, EmbeddedDocument, EmbeddedDocumentField, BooleanField
from .base_document import BaseDocument

    
# class Address(EmbeddedDocument):
#     street = StringField(default="", required=True)
#     city = StringField(default="", required=True)
#     postalCode = StringField(default="", required=True)
#     country = StringField(default="", required=True)

class Client(BaseDocument):
    name = StringField(required=True, default="")
    siret = StringField(required=True, default="")
    vat_number = StringField(required=True, default="")
    logo_url = StringField(required=False, default="")
    clientType = StringField(required=True, default="")
    documentLanguage = StringField(required=True, default="")
    documentCurrency = StringField(required=True, default="")
    contact = EmbeddedDocumentField(Contact, required=True)
    facturation = EmbeddedDocumentField(Address, required=True)
    delivery = EmbeddedDocumentField(Address, required=False)
    company_id = StringField(required=True, default="")
    contactadresse = EmbeddedDocumentField(Address, required=True)
    userContactAsDelivery= BooleanField(required=True, default=False)
    userContactAsFacuration= BooleanField(required=True, default=False)
    meta = {
        'collection': 'clients',
        "strict": False
    }
    