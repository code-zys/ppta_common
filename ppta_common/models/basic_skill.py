from mongoengine import  StringField, EmbeddedDocument

class BasicSkill(EmbeddedDocument):
    name = StringField(required=True)
    description = StringField(required=False)
