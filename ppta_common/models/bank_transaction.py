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
    date = IntField(required=True)
    type = StringField(required=True)
    value = IntField(required=True)
    
    original_value = IntField()
    original_currency = StringField()
    formatted_value = StringField(required=True)

    company = ReferenceField(Company, required=True)

    bank_account = ReferenceField(BankAccount)
    source = StringField(
        choices=[status.value for status in BankProviderEnum],
        required=True
    )
    source_transaction_id=StringField()

    data = DictField(required=True)

    meta = {
        'collection': 'bank_transactions',
        "strict": False,
        'indexes': [
            {
                'fields': ['company', 'bank_account','source_transaction_id'],
                'unique': True 
            }
        ]
    }