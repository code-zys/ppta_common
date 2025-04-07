from mongoengine import  StringField, ListField, BooleanField, IntField, EmbeddedDocumentField, ReferenceField
from .base_document import BaseDocument
from .note import Note
from .time_range import TimeRange
from .company import Company
from .workplace import Workplace


class Coach(BaseDocument):
    """
    Coach model
    """
    name = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    phone = StringField(max_length=50, required=True)
    language = ListField(StringField(), required=True)
    min_booking_time = IntField(required=False)
    workplaces = ListField(EmbeddedDocumentField('Workplace'), required=False) 
    member_id = StringField(required=False)
    is_coaching_profile_visible = BooleanField(default=True)
    is_profile_verified= BooleanField(default=False)
    is_profile_disabled_by_admin = BooleanField(default=False)
    company_approved_coach = BooleanField(default=True)
    company = ReferenceField(Company, required=True)
    bio = StringField(required=False)
    region = StringField(required=False)
    profile_picture = StringField(required=False)
    slug = StringField(required=True)