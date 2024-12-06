from mongoengine import (
    IntField,
    StringField,
    DateTimeField,
    BooleanField,
    fields,
    ReferenceField
)
from .base_document import BaseDocument
from .company import Company


class PowensConnection(BaseDocument):
    connection_id = IntField(required=True)
    id_user = IntField(required=True)
    id_connector = IntField(required=True)
    last_update = DateTimeField(required=True)
    created = DateTimeField(required=True)
    active = BooleanField(default=True)
    last_push = fields.DateTimeField(null=True)
    next_try = fields.DateTimeField(null=True)
    state = StringField(null=True)
    error = StringField(null=True)
    error_message = StringField(null=True)
    expire = DateTimeField(null=True)
    id_bank = IntField(required=True)
    connector_uuid = StringField(null=True)
    company = ReferenceField(Company)


    meta = {
        'collection': 'powens_connection'
    }
