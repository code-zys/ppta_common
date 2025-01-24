from mongoengine import EmbeddedDocument, StringField, IntField

class Skill(EmbeddedDocument):
    code = StringField(required=True)
    name = StringField(required=True)
    percent = IntField(required=True)