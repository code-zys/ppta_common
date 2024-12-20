from mongoengine import StringField, EmbeddedDocument

class Condition(EmbeddedDocument):
    discount = StringField(default="", required=True)
    panality = StringField(default="", required=True)
    indeminity = StringField(default="", required=True)