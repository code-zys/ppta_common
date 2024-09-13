from mongoengine import EmbeddedDocument, StringField, IntField

class TimeZone(EmbeddedDocument):
    name = StringField()
    offset = IntField()