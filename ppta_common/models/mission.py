from mongoengine import Document, StringField, DateTimeField, ReferenceField, EnumField
from .company import Company
from .member import Member
from .application import Application
from ..enums.mission_status_enum import MissionStatus

class Mission(Document):
    title = StringField(required=True)
    description = StringField()
    start_date = DateTimeField(required=True)
    end_date = DateTimeField()
    
    consultant = ReferenceField(Member, required=True)
    commercial = ReferenceField(Member)
    final_client = ReferenceField(Company, required=True)
    status = EnumField(MissionStatus, required=True, description="Status of the mission", default=MissionStatus.PENDING)
    application = ReferenceField(Application,required=True)
    meta = {'collection': 'missions'}