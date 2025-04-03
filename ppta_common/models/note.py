from mongoengine import EmbeddedDocument, StringField
from ..enums.rating_level import EnumRatingLevel

class Note(EmbeddedDocument):
    name = StringField(required=True)
    value = StringField(choices=[e.value for e in EnumRatingLevel], required=True)
    comment = StringField(required=False)
    client = StringField(required=True)