from mongoengine import (
    Document,
    IntField,
    StringField,
    FloatField,
    BooleanField,
    DateTimeField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    DictField,
    NULLIFY,
    ReferenceField
)
from .powens_connection import PowensConnection
from .base_document import BaseDocument


class PowenCurrency(EmbeddedDocument):
    id = StringField(required=True)
    symbol = StringField()
    prefix = BooleanField(default=False)
    crypto = BooleanField(default=False)
    precision = IntField()
    marketcap = FloatField(null=True)
    datetime = DateTimeField(null=True)
    name = StringField(null=True)

class PowenAccount(BaseDocument):
    account_id = IntField(required=True)
    id_connection = IntField(required=True)
    id_user = IntField(required=True)
    id_source = IntField(required=True)
    id_parent = IntField(null=True)
    number = StringField(required=True)
    webid = StringField(required=True)
    original_name = StringField()
    balance = FloatField(required=True)
    coming = FloatField(null=True)
    display = BooleanField(default=True)
    last_update = DateTimeField(required=True)
    deleted = DateTimeField(null=True)
    disabled = BooleanField(null=True)
    iban = StringField()
    currency = EmbeddedDocumentField(PowenCurrency, null=True)
    id_type = IntField(required=True)
    bookmarked = IntField(default=0)
    name = StringField(required=True)
    error = StringField(null=True)
    usage = StringField(null=True)
    ownership = StringField(null=True)
    company_name = StringField(null=True)
    opening_date = DateTimeField(null=True)
    bic = StringField()
    coming_balance = FloatField(required=True)
    formatted_balance = StringField()
    type = StringField(choices=["checking", "savings", "loan", "other"], default="checking")
    information = DictField()
    loan = DictField()
    powen_connection = ReferenceField(PowensConnection)

    meta = {
        "collection": "powen_accounts",
        "strict": False,
        "cascade": True,
        "cascade_kwargs": {"delete_rule": NULLIFY}
    }
