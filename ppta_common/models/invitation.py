from mongoengine import StringField, ReferenceField, ListField

from .base_document import BaseDocument
from .company import Company
from .shared_document import SharedDocument
from ..utils.enums import EnumOriginInvitation, EnumSatusInvitation
from .user import User

class Invitation(BaseDocument):
    user = ReferenceField(User, required=False)
    user_email = StringField(required=False)
    company =  ReferenceField(Company)
    status = StringField(choices=[e.value for e in EnumSatusInvitation], required=True)
    origin = StringField(choices=[e.value for e in EnumOriginInvitation], required=True)
    shared_documents = ListField(ReferenceField(SharedDocument))
   