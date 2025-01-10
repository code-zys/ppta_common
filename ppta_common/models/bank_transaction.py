from .company import Company
from .category import Category
from .invoice_class import InvoiceClass
from .base_document import BaseDocument
from .client import Client
from mongoengine import (
    IntField,
    StringField,
    DictField,
    ReferenceField,
    FloatField
)
from .bank_account import BankAccount
from ..enums.bank_provider_enum import BankProviderEnum
from ..enums.bank_transaction_type_enum import BankTransactionTypeEnum

class BankTransaction(BaseDocument):
    wording = StringField(required=True)
    date = IntField(required=True)
    type = StringField(
        choices=[status.value for status in BankTransactionTypeEnum],
        required=True
    )
    value = FloatField(required=True)
    original_value = FloatField()
    original_currency = StringField()
    formatted_value = StringField(required=True)

    company = ReferenceField(Company, required=True)
    category = ReferenceField(Category, required=False)
    provider = ReferenceField(InvoiceClass, required=False)
    method = StringField(required=True)
    client = ReferenceField(Client)
    bank_account = ReferenceField(BankAccount)
    source = StringField(
        choices=[status.value for status in BankProviderEnum],
        required=True
    )
    source_transaction_id=StringField()
    currency_name = StringField(required=True)
    pricing = DictField(required = True)

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