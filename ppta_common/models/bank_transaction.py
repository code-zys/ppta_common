from .company import Company
from .base_document import BaseDocument
from mongoengine import (
    IntField,
    StringField,
    DictField,
    ReferenceField,
    DateField
)
from .bank_account import BankAccount
from ..enums.bank_provider_enum import BankProviderEnum


class BankTransaction(BaseDocument):
    wording = StringField(required=True)
    date = DateField(required=True)
    type = StringField(required=True)
    value = IntField(required=True)
    
    original_value = IntField(required=True)
    original_currency = StringField(required=True)
    formatted_value = StringField(required=True)

    company = ReferenceField(Company)

    bank_account = ReferenceField(BankAccount)
    source = StringField(
        choices=[status.value for status in BankProviderEnum],
        required=True
    )

    data = DictField(required=True)

    meta = {
        'collection': 'bank_transactions',
        "strict": False
    }