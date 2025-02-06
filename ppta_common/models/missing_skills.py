from mongoengine import Document, StringField

class MissingSkills(Document):
    code = StringField(required=True)
    type = StringField(required=True, default='skill')
    title = StringField(required=True)

    meta = {
        'auto_create_index': False,
        'id_field': None
    }