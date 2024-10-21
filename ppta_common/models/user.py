from mongoengine import EmbeddedDocumentField, StringField, Document, BooleanField

from .timezone import TimeZone
from ..utils.enums import EnumUserType
from .professional_info import ProfessionalInfo

class User(Document):
    firstname = StringField(required=False, default="")
    lastname = StringField(required=False, default="")
    picture = StringField(required=False, default="")
    userId = StringField(required=False, default="")
    email = StringField(required=False, default="")
    is_certified_accountant = BooleanField(required=True, default=False)
    is_contractor = BooleanField(required=True, default=False)
    is_employee = BooleanField(required=True, default=False)
    is_freelance = BooleanField(required=True, default=False)
    timeZone = EmbeddedDocumentField(TimeZone, default = None)
    professional_info = EmbeddedDocumentField(ProfessionalInfo, default=None)
    user_type = StringField(choices=[e.value for e in EnumUserType], required=False)
    # enabled = BooleanField(required=False, default=False)
    # disabledByAdmin = BooleanField(required=False, default=False)
    meta = {
        'collection': 'users',
        "strict": False
    }