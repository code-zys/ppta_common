from mongoengine import StringField, EmbeddedDocument

class Contact(EmbeddedDocument):
    email = StringField(default="", required=True)
    phone = StringField(default="", required=True)