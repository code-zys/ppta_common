from mongoengine import EmbeddedDocument, StringField, BooleanField, ListField, EmbeddedDocumentField, IntField
from .skill import Skill

class Workplace(EmbeddedDocument):
    """
    Workplace embedded document
    """
    code = StringField(max_length=50, required=False)
    client = StringField(max_length=50, required=False)
    position = StringField(max_length=50, required=False)
    skills = ListField(EmbeddedDocumentField(Skill), required=False)
    description = StringField(required=False)
    verified = BooleanField(required=False, default=False)
    verified_at = IntField(required=False)
    start_date = IntField(required=False)
    end_date = IntField(required=False)