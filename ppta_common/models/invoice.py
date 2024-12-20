from mongoengine import IntField, StringField, ReferenceField, EmbeddedDocumentField, BooleanField, ListField
from .client import Client
from .total import Totals
from .setting import Setting
from .company import Company
from .base_document import BaseDocument
from .invoice_template import InvoiceTemplate
from ..enums.invoice_status_enum import EnumInvoiceStatus

class Invoice(BaseDocument):
    number = StringField(required=True, default="")
    issue_date = IntField(required=True, default=None)
    due_date =IntField(required=True, default=None)
    delivery_date = IntField(required=True, default=None)
    status = StringField(choices=[e.value for e in EnumInvoiceStatus], required=True, default=EnumInvoiceStatus.UNPAID.value)
    client = ReferenceField(Client)
    invoice_items = ListField(ReferenceField('InvoiceItem'))
    total = EmbeddedDocumentField(Totals, required=True)
    # payment_details = EmbeddedDocumentField(PaymentDetails, required=True)
    settings = ReferenceField(Setting,required=True)
    company = ReferenceField(Company,required=True)
    notes = StringField(required=False, default="")
    template = ReferenceField(InvoiceTemplate)
    sended = BooleanField(required=True,default=False)
    meta = {
        'collection': 'printed_invoices',
        "strict": False
    }