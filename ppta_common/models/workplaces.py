from mongoengine import EmbeddedDocument, StringField, BooleanField, ListField
from .skill import Skill

class Workplace(EmbeddedDocument):
    """
    Workplace embedded document
    """
    code = StringField(max_length=50, required=False)
    client = StringField(max_length=50, required=False)
    position = StringField(max_length=50, required=False)
    skills = ListField(Skill, required=False)
    description = StringField(required=False)
    verified = BooleanField(required=False, default=False)