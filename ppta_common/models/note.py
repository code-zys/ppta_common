from mongoengine import StringField
from ..enums.rating_level_enum import EnumRatingLevel
from .base_document import BaseDocument

class Note(BaseDocument):
    name = StringField(required=True)
    value = StringField(choices=[e.value for e in EnumRatingLevel], required=True)
    comment = StringField(required=False)
    client = StringField(required=True)