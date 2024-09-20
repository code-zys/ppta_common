
from mongoengine import StringField, EmbeddedDocument, DateTimeField, ObjectIdField, BooleanField

class ProfessionalInfo(EmbeddedDocument):
    work_station = StringField(required=True)
    phone_number = StringField(required=True)
    professional_email = StringField(required=True)
    start_date = DateTimeField(required=True)
    validation_date = DateTimeField(default=None)
    company_id = ObjectIdField(required=True)
    approved = BooleanField(required=False)