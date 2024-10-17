from mongoengine import Document, StringField, ReferenceField, ListField, DateTimeField
from .user import User
from .company import Company
from datetime import datetime

class Notification(Document):
    room = StringField(required=True)
    message = StringField(required=True)
    notification_type = StringField(required=False)
    object = StringField(required=False)
    status = StringField(required=False)
    to_user = ReferenceField(User, required=False)
    to_company = ReferenceField(Company, required=False)
    to_company_role = ListField(StringField(choices=["admin", "manager"]), required=False)
    datetime = DateTimeField(default=datetime.utcnow)
   