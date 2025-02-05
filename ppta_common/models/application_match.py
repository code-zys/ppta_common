from mongoengine import FloatField, EmbeddedDocument

class ApplicationMatch(EmbeddedDocument):
    skill = FloatField(required=True)
    experience = FloatField(required=True)
    language = FloatField(required=True)
    knowhow = FloatField(required=True)