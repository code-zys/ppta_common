from mongoengine import EmbeddedDocument, StringField, IntField

class Skill(EmbeddedDocument):
    code = StringField(required=True)
    name = StringField(required=True)
    percent = IntField(required=False)
    link_to_video = StringField(required=False)
    description = StringField(required=False)