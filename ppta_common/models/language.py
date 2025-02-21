from mongoengine import EmbeddedDocument, StringField
from ..enums.language_level_enum import EnumLanguageLevel

class Language(EmbeddedDocument):
    code = StringField(required=True)
    titled = StringField(required=True)
    level = StringField(choices=[e.value for e in EnumLanguageLevel], required=True)