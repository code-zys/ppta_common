from .base_document import BaseDocument
from mongoengine import (
    IntField,
    StringField,
    FloatField,
    BooleanField,
    DictField
)

class PowensTransaction(BaseDocument):
    transaction_id = IntField(required=True)
    account_id = IntField(required=True)
    webid = StringField(required=True, default="")
    application_date = StringField(required=True, default="")
    date = StringField(required=True, default="")
    datetime = StringField(required=True, default="")
    value = FloatField(required=True, default=0.0)
    state = StringField(required=True, default="")
    scraped_date = StringField(required=True, default="")
    coming = BooleanField(required=True, default=False) 
    active = BooleanField(required=True, default=True) 
    cluster_id = StringField(required=False, default=None)
    comment = StringField(required=False, default=None)
    last_update = StringField(required=True, default=None)
    original_value = FloatField(required=False, default=None)
    original_gross_value = StringField(required=False, default=None)
    original_currency = DictField(required=False, default=None)
    commission = FloatField(required=False, default=None)
    commission_currency = StringField(required=False, default=None)
    card = StringField(required=True, default=None)
    type = StringField(required=True, default=None)
    new = BooleanField(required=True, default=False)
    formatted_value = StringField(required=True, default=None)
    documents_count = IntField(required=True, default=0)
    informations = DictField()
    country = StringField(required=False, default=None)
    counterparty = StringField(required=False, default=None)
    meta = {
        'collection': 'powen_transactions',
        "strict": False
    }