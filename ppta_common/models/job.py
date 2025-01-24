from mongoengine import EmbeddedDocument, StringField

class Job(EmbeddedDocument):
    code = StringField(required=True)
    name = StringField(required=True)