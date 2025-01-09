from mongoengine import ReferenceField, StringField, EmbeddedDocumentField, IntField
from .base_document import BaseDocument
from .company import Company
from .contact import Contact
from ..enums.settings_type_enum import SettingType
from ..enums.payment_condition_enum import EnumPaymentCondition
from ..enums.transaction_type_enum import TransactionType
from .condition import Condition
from .payment_detail import PaymentDetails
from .payment_condition import PaymentCondition

class Setting(BaseDocument):
    terms_and_conditions = StringField(required=False, default="")
    company = ReferenceField(Company, required=True)
    invoice_format = StringField(default="FAC-(AAAA)-(MM)", max_length=50)
    language = StringField(default="fr", max_length=5)
    settingtype = StringField(choices=[e.value for e in SettingType], required=True, default=SettingType.INVOICE.value)
    transactiontype = StringField(choices=[e.value for e in TransactionType], required=True)
    conditions = EmbeddedDocumentField(Condition, required=False)
    next_invoice_number = IntField(required=False, default=1)
    vat_number = StringField(required=True, default="") 
    payment_condition= StringField(choices=[e.value for e in EnumPaymentCondition], required=True, default=EnumPaymentCondition.ON_RECEIPT.value)
    custom_payment_condition= EmbeddedDocumentField(PaymentCondition, required=False, default=None)
    social_capital= StringField(required=False, default="")
    rcs= StringField(required=False, default="")
    contact = EmbeddedDocumentField(Contact, required=True)
    payment_details = EmbeddedDocumentField(PaymentDetails, required=False) #TODO:ajouter ceci dans les commonts
    tax_rate = IntField(required=True)
    meta = {
        'collection': 'settings',
        "strict": False
    }