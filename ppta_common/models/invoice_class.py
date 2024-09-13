from mongoengine import StringField, ListField, EmbeddedDocumentField, EnumField, IntField, BooleanField, ObjectIdField
from .base_document import BaseDocument
from .collect_rule import CollectRule
from .delivery_rule import DeliveryRule
from ..utils.enums import EnumRole, InvoiceClassType
from .user_metadata import UserMetadata

class InvoiceClass(BaseDocument):
    supplier = StringField()
    name = StringField()
    code = StringField()

    type = EnumField(InvoiceClassType)
    description = StringField()
   
    created_at = IntField(required=True)
    updated_at = IntField(default=None)
    deleted = BooleanField(default=False)
    deleted_at = IntField(default=None)
    created_by = EmbeddedDocumentField(UserMetadata, default=None)  
    updated_by = EmbeddedDocumentField(UserMetadata, default=None)
    deleted_by = EmbeddedDocumentField(UserMetadata, default=None)
    
    collect_rules = ListField(EmbeddedDocumentField(CollectRule))
    delivery_rules = ListField(EmbeddedDocumentField(DeliveryRule))
    company_id = ObjectIdField(required=True)
    only_visible_by = ListField(StringField(choices=[e.value for e in EnumRole]), default = [])
    can_upload = ListField(StringField(choices=[e.value for e in EnumRole]), default = [])

    meta = {'collection': 'invoice_class',
             'strict': False
            }
    
    def __str__(self):
        return str(self.id)