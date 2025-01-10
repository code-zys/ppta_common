from mongoengine import StringField, BooleanField, ReferenceField
from .company import Company
from .base_document import BaseDocument

class Category(BaseDocument):
    name = StringField(required=True)
    number = StringField(required=False)
    code = StringField(required=True, unique=True)
    description = StringField(max_length=500)
    is_system = BooleanField(default=False)
    company = ReferenceField(Company, required=False)
    active = BooleanField(required=True, default=True)

    meta = {
        'collection': 'categories',
        'indexes': [
            'code',
            'company',
        ]
    }