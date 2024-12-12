from mongoengine import (
    IntField,
    StringField,
    DictField,
    ReferenceField,
    DateField
)
from .bank_connection import BankConnection
from .base_document import BaseDocument
from ..enums.bank_provider_enum import BankProviderEnum

class BankAccount(BaseDocument):
    name = StringField(required=True)
    number = StringField(required=True)
    currency_name = StringField(required=True)
    currency_symbol = StringField(required=True)
    type = StringField(required=True)
    balance = IntField(required=True)


    bank_connection = ReferenceField(BankConnection)

    from_sync_date =  DateField(required=False)
    to_sync_date = DateField(required = False)
    last_sync_date = DateField(required=False)

    source = StringField(
        choices=[status.value for status in BankProviderEnum],
        required=True
    )

    data = DictField(required=True)

    meta = {
        "collection": "bank_accounts",
        "strict": False
    }