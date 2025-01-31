from mongoengine import EmbeddedDocument, StringField

class Function(EmbeddedDocument):
    code = StringField(required=True)
    name = StringField(required=True)