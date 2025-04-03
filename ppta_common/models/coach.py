from mongoengine import  StringField, ListField, BooleanField, IntField, EmbeddedDocumentField, ReferenceField
from .base_document import BaseDocument
from .note import Note
from .time_range import TimeRange
from .workplaces import Workplace

class Coach(BaseDocument):
    """
    Coach model
    """
    name = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    phone = StringField(max_length=50, required=True)
    language = ListField(StringField(), required=True)
    min_booking_time = IntField(required=False)
    notes = ListField(EmbeddedDocumentField(Note), required=False)
    workplaces = ListField(ReferenceField(Workplace), required=False)
    member_id = StringField(required=False)
    is_coaching_profile_visible = BooleanField(default=False)
    is_profile_verified= BooleanField(default=False)
    is_profile_disabled_by_admin = BooleanField(default=False)
    company_approved_coach = BooleanField(default=True)
    un_avalaible_times = ListField(EmbeddedDocumentField(TimeRange), required=False)