from mongoengine import EmbeddedDocument, StringField

class UserMetadata(EmbeddedDocument):
    id = StringField()
    fullname = StringField()
    picture = StringField(default="")
    user_id = StringField()
    email = StringField()
