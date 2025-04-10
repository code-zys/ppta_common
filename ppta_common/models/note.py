from mongoengine import StringField,ReferenceField
from ..enums.rating_level_enum import EnumRatingLevel
from .base_document import BaseDocument
from .coaching import Coaching

class Note(BaseDocument):
    name = StringField(required=True)
    value = StringField(choices=[e.value for e in EnumRatingLevel], required=True)
    comment = StringField(required=False)
    client = StringField(required=True)
    coach_id = StringField(required=True)
    coaching_id = ReferenceField(Coaching, required=True)
