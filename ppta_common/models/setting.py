from mongoengine import ReferenceField, StringField, EmbeddedDocumentField, IntField
from .base_document import BaseDocument
from .company import Company
from .client import Contact
from ..enums.settings_type_enum import SettingType
from ..enums.transaction_type_enum import TransactionType
from .condition import Condition

class Setting(BaseDocument):
    terms_and_conditions = StringField(required=False, default="")
    company = ReferenceField(Company, required=True)
    invoice_format = StringField(default="FAC-(AAAA)-(MM)-(6num)", max_length=50)
    currency = StringField(default="EUR", max_length=5)
    language = StringField(default="fr", max_length=5)
    settingtype = StringField(choices=[e.value for e in SettingType], required=True, default=SettingType.iNVOICE.value)
    transactiontype = StringField(choices=[e.value for e in TransactionType], required=True)
    conditions = EmbeddedDocumentField(Condition, required=False)
    next_invoice_number = IntField(required=False, default=1)
    vat_number = StringField(required=True, default="") 
    payment_condition= StringField(required=False, default="")
    social_capital= StringField(required=False, default="")
    rcs= StringField(required=False, default="")
    contact = EmbeddedDocumentField(Contact, required=True)
    
    meta = {
        'collection': 'settings',
        "strict": False
    }