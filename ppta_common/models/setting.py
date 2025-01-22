from mongoengine import ReferenceField, StringField, EmbeddedDocumentField, IntField
from .base_document import BaseDocument
from .company import Company
from .contact import Contact
from ..enums.settings_type_enum import SettingType
from ..enums.vat_payment_condition_enum import EnumVatPaymentCondition
from .condition import Condition
from .payment_detail import PaymentDetails

class Setting(BaseDocument):
    company = ReferenceField(Company, required=True)
    invoice_format = StringField(default="FAC-(AAAA)-(MM)", max_length=50)
    settingtype = StringField(choices=[e.value for e in SettingType], required=True, default=SettingType.INVOICE.value)
    conditions = EmbeddedDocumentField(Condition, required=False)
    next_invoice_number = IntField(required=False, default=1)
    vat_number = StringField(required=True, default="") 
    payment_condition= StringField(choices=[e.value for e in EnumVatPaymentCondition], required=True, default=EnumVatPaymentCondition.ON_RECEIPTS.value)
    social_capital= StringField(required=False, default="")
    rcs= StringField(required=False, default="")
    contact = EmbeddedDocumentField(Contact, required=True)
    payment_details = EmbeddedDocumentField(PaymentDetails, required=False) #TODO:ajouter ceci dans les commonts
    tax_rate = IntField(required=True)
    meta = {
        'collection': 'settings',
        "strict": False
    }