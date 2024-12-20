from mongoengine import StringField, IntField, ListField, BooleanField, EmbeddedDocumentField, ReferenceField
from .base_document import BaseDocument
from .client import Client
from .setting import Setting
from .invoice_template import InvoiceTemplate
from .quote_version import QuoteVersion
from .quote_item import QuoteItem
from .company import Company
from .total import Totals

class Quote(BaseDocument):
    number = StringField(required=True, default="")
    issue_date = IntField(required=True, default=None)   
    validity_date = IntField(required=True, default=None)   
    client = ReferenceField(Client, required=True)   
    quote_items = ListField(EmbeddedDocumentField(QuoteItem), required=True)   
    total = EmbeddedDocumentField(Totals, required=True)   
    company = ReferenceField(Company, required=True)  
    settings = ReferenceField(Setting, required=True)   
    template = ReferenceField(InvoiceTemplate, required=False)   
    notes = StringField(required=False, default="")   
    is_accepted = BooleanField(default=False)   
    pdf_link = StringField(required=False, default="")
    send_quote_at_generation = BooleanField(default=False)
    is_send = BooleanField(default=False) 
    quote_versions = ListField(EmbeddedDocumentField(QuoteVersion), required=False)   
    
    meta = {
        'collection': 'quotes',
        "strict": False
    }