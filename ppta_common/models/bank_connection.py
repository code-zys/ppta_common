from mongoengine import (
    IntField,
    StringField,
    DateTimeField,
    BooleanField,
    fields,
    ReferenceField,
    DictField
)
from .base_document import BaseDocument
from .company import Company
from ..enums.bank_provider_enum import BankProviderEnum


class BankConnection(BaseDocument):
    title = StringField()
    company = ReferenceField(Company)
    institution_name = StringField()
    source = StringField(
        choices=[status.value for status in BankProviderEnum],
        required=True
    )
    expire = DateTimeField()
    active = BooleanField(required=True)
    data = DictField(required=True)

    meta = {
        'collection': 'bank_connections'
    }
