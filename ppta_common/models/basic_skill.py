from mongoengine import  StringField, EmbeddedDocumentField

class BasicSkill(EmbeddedDocumentField):
    name = StringField(required=True)
    description = StringField(required=False)
