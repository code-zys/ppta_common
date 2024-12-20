from mongoengine import StringField, IntField, BooleanField, ReferenceField, ListField, EmbeddedDocumentField
from .base_document import BaseDocument
from .company import Company
from .invoice_template import InvoiceTemplate
from .setting import Setting
from .client import Client
from ..enums.period_enum import EnumPeriod
from ..enums.payment_condition_enum import EnumPaymentCondition
from ..enums.custom_frequency_enum import EnumCustomFrequency
from .invoice_item import InvoiceItem

class RecurringInvoice(BaseDocument):
    description = StringField(required=False, default="")
    active = BooleanField(required=False, default=False)
    starting_date =IntField(required=True, default=None)
    frequency = StringField(choices=[e.value for e in EnumPeriod], required=False)
    is_frequency_custom = BooleanField(required=True,default=False)
    custom_frequency = IntField(required=False, default=None)
    custom_frequency_unit = StringField(choices=[e.value for e in EnumCustomFrequency], required=False)
    client = ReferenceField(Client)
    invoice_items = ListField(EmbeddedDocumentField(InvoiceItem), required=True)
    settings = ReferenceField(Setting,required=True)
    template = ReferenceField(InvoiceTemplate)
    ending_date = IntField(required=True, default=None)
    send_invoice_at_generation = BooleanField(required=True,default=False)
    company = ReferenceField(Company,required=True)
    payment_condition = StringField(choices=[e.value for e in EnumPaymentCondition], required=False)
    custom_payment_condition = IntField(required=False, default=None)
    # payment_details = EmbeddedDocumentField(PaymentDetails, required=True) #TODO: verifier l'utiliter
    meta = {
        'collection': 'recurring_invoices',
        "strict": False
    }