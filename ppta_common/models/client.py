from mongoengine import StringField, EmbeddedDocumentField, BooleanField, ReferenceField
from .base_document import BaseDocument
from .contact import Contact
from .address import Address
from ..enums.currency_type_enum import EnumCurencyType
from .company import Company

class Client(BaseDocument):
    name = StringField(required=True, default="")
    siret = StringField(required=True, default="")
    vat_number = StringField(required=True, default="")
    logo_url = StringField(required=False, default="")
    clientType = StringField(required=True, default="")
    documentLanguage = StringField(required=True, default="")
    documentCurrency = StringField(required=True,choices=[e for e in EnumCurencyType], default=EnumCurencyType.EUR)
    contact = EmbeddedDocumentField(Contact, required=True)
    facturation = EmbeddedDocumentField(Address, required=False)
    delivery = EmbeddedDocumentField(Address, required=False)
    company = ReferenceField(Company, required=True)
    contactaddress = EmbeddedDocumentField(Address, required=True)
    userContactAsDelivery= BooleanField(required=True, default=False)
    userContactAsFacuration= BooleanField(required=True, default=False)
    meta = {
        'collection': 'clients',
        "strict": False
    }