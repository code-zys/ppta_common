from mongoengine import EmbeddedDocument, StringField

class Workplace(EmbeddedDocument):
    region = StringField(required=True, description="Region where the workplace is located")
    town = StringField(required=True, description="Town where the workplace is located")