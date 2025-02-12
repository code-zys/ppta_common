from mongoengine import Document, StringField, DateTimeField, ReferenceField
from .company import Company
from .member import Member
from .application import Application

class Mission(Document):
    title = StringField(required=True)
    description = StringField()
    start_date = DateTimeField(required=True)
    end_date = DateTimeField()
    
    consultant = ReferenceField(Member, required=True)
    commercial = ReferenceField(Member)
    client = ReferenceField(Company, required=True)
    
    application = ReferenceField(Application,required=True)
    meta = {'collection': 'missions'}