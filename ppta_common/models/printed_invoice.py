from mongoengine import StringField, DateField, ReferenceField, BooleanField, DictField, ListField, EmbeddedDocumentField
from .client import Client
from .total import Totals
from .setting import Setting
from .invoice_template import InvoiceTemplate
from .recurring_invoice import RecurringInvoice
from .company import Company
from .base_document import BaseDocument
from .invoice_item import InvoiceItem
from ..enums.invoice_status_enum import EnumInvoiceStatus
from ..enums.invoice_state_enum import EnumInvoiceState

class PrintedInvoice(BaseDocument):
    number = StringField(required=True, default="")
    emitted_at = DateField(required=True, default=None)
    due_date =DateField(required=True, default=None)
    status = StringField(choices=[e.value for e in EnumInvoiceStatus], required=True, default=EnumInvoiceStatus.UNPAID.value)
    state = StringField(choices=[e.value for e in EnumInvoiceState], required=True, default=EnumInvoiceState.INITIAL.value)
    client = ReferenceField(Client)
    printed_invoice_items =ListField(EmbeddedDocumentField(InvoiceItem), required=True)
    total = EmbeddedDocumentField(Totals, required=True)
    settings = ReferenceField(Setting,required=True)
    company = ReferenceField(Company,required=True)
    notes = StringField(required=False, default="")
    template = ReferenceField(InvoiceTemplate)
    sended = BooleanField(required=True,default=False)
    recuring_invoice_template = ReferenceField(RecurringInvoice,required=False)
    order_number = StringField(required=False, default="")
    pdf_link = StringField(required=False, default="")
    
    pricing = DictField(field=EmbeddedDocumentField(Totals), required=False, default={})
    
    meta = {
        'collection': 'printed_invoices',
        "strict": False
    }