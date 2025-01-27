from mongoengine import EmbeddedDocument, StringField, IntField

class KnowHow(EmbeddedDocument):
    code = StringField(required=True)
    name = StringField(required=True)