from mongoengine import StringField, ReferenceField, ListField, BooleanField, IntField, EmbeddedDocumentField
from .user_metadata import UserMetadata

from .base_document import BaseDocument
from .company import Company
from .shared_document import SharedDocument
from ..utils.enums import EnumOriginInvitation, EnumSatusInvitation
from .user import User

class Invitation(BaseDocument):
    user = ReferenceField(User, required=False)
    user_email = StringField(required=False)
    company =  ReferenceField(Company)
    company_email = StringField(required=False)
    status = StringField(choices=[e.value for e in EnumSatusInvitation], required=True)
    origin = StringField(choices=[e.value for e in EnumOriginInvitation], required=True)
    shared_documents = ListField(ReferenceField(SharedDocument))
    can_manage_subscription = BooleanField(required=False,default=False)
    updated_can_manage_subscription_at = IntField(required=True)
    update_can_manage_subscription_by = EmbeddedDocumentField(UserMetadata, default=None)
