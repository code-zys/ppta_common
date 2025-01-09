from mongoengine import StringField, EmbeddedDocument

class Condition(EmbeddedDocument):
    discount = StringField(default="", required=True)
    penality = StringField(default="", required=True)
    indeminity = StringField(default="", required=True)