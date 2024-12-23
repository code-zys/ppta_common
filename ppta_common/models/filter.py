from .base_document import BaseDocument
from mongoengine import StringField, DictField, ReferenceField
from .company import Company
from ..enums.filter_type_enum import EnumFilterType


class Filter(BaseDocument):
    name = StringField(required=True)
    type = StringField(
        choices=[status.value for status in EnumFilterType],
        required=True
    )
    payload = DictField()
    company = ReferenceField(Company, required=True)

    meta = {
        'collection': 'filters',
        "strict": False,
        'indexes': [
            {
                'fields': ['company', 'name','type'],
                'unique': True 
            }
        ]
    }