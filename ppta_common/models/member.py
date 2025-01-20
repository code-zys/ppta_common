from mongoengine import StringField, EmbeddedDocumentField, BooleanField, ReferenceField, IntField

from .base_document import BaseDocument
from .company import Company
from .professional_info import ProfessionalInfo
from .user_metadata import UserMetadata
from .user import User
from ..utils.enums import EnumRole, EnumUserType

class Member(BaseDocument):
    professional_info = EmbeddedDocumentField(ProfessionalInfo, default=None)
    role = StringField(choices=[e.value for e in EnumRole], required=True)
    user = ReferenceField(User)
    company = ReferenceField(Company)
    approved = BooleanField(required=True)
    approved_at = IntField(default=None)
    approved_by = EmbeddedDocumentField(UserMetadata, default=None) 
    user_type = StringField(choices=[e.value for e in EnumUserType], required=True)
    is_consultant = BooleanField(default=False)
    is_commercial = BooleanField(default=False)