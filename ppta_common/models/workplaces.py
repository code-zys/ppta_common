from mongoengine import EmbeddedDocumentField, StringField, BooleanField, ListField

class Workplace(EmbeddedDocumentField):
    """
    Workplace embedded document
    """
    code = StringField(max_length=50, required=False)
    client = StringField(max_length=50, required=False)
    position = StringField(max_length=50, required=False)
    skills = ListField(StringField(), required=False)
    description = StringField(required=False)
    verified = BooleanField(required=False, default=False)