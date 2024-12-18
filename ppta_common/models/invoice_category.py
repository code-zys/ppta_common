from mongoengine import StringField, BooleanField, ReferenceField
from .company import Company
from .base_document import BaseDocument

class InvoiceCategory(BaseDocument):
    name = StringField(required=True, max_length=255)
    code = StringField(required=True, unique=True, max_length=50)
    description = StringField(max_length=500)
    is_system = BooleanField(default=False)
    company = ReferenceField(Company, required=False)

    meta = {
        'collection': 'invoice_categories',
        'indexes': [
            'code',
            'company',
        ]
    }