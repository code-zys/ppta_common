from mongoengine import StringField, IntField, BooleanField, ReferenceField, ListField, EmbeddedDocumentField
from .base_document import BaseDocument
from .company import Company
from .invoice_template import InvoiceTemplate
from .setting import Setting
from .client import Client
from ..enums.payment_condition_enum import EnumPaymentCondition
from .invoice_item import InvoiceItem
from .programmation_details import Programmation_details
from ..enums.mesure_unit_enum import EnumMesureUnit
from .exoneration_nature import ExonerationNature
from .discount import Discount

class RecurringInvoice(BaseDocument):
    description = StringField(required=False, default="")
    active = BooleanField(required=False, default=False)
    programmation_details=EmbeddedDocumentField(Programmation_details)
    client = ReferenceField(Client)
    invoice_items = ListField(EmbeddedDocumentField(InvoiceItem), required=True)
    settings = ReferenceField(Setting,required=True)
    template = ReferenceField(InvoiceTemplate)
    send_invoice_at_generation = BooleanField(required=True,default=False)
    company = ReferenceField(Company,required=True)
    payment_condition = StringField(choices=[e.value for e in EnumPaymentCondition], required=False)
    custom_payment_condition = IntField(required=False, default=None)
    custom_payment_condition_unit = StringField(choices=[e.value for e in EnumMesureUnit],required=False )
    order_number = StringField(required=False, default=None)
    discount = EmbeddedDocumentField(Discount, required=False, default=None)
    exoneration = ReferenceField(ExonerationNature, required=False, default=None)
    meta = {
        'collection': 'recurring_invoices',
        "strict": False
    }