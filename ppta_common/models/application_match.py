from .base_document import BaseDocument
from mongoengine import FloatField

class ApplicationMatch(BaseDocument):
    skill = FloatField(required=True)
    experience = FloatField(required=True)
    language = FloatField(required=True)
    knowhow = FloatField(required=True)