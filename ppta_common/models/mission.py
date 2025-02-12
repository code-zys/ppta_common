from mongoengine import StringField, DateTimeField, ReferenceField, EnumField
from .company import Company
from .member import Member
from .application import Application
from ..enums.mission_status_enum import MissionStatus
from .base_document import BaseDocument
class Mission(BaseDocument):
    title = StringField(required=True)
    description = StringField()
    start_date = DateTimeField(required=True)
    end_date = DateTimeField()
    
    consultant = ReferenceField(Member, required=False)
    commercial = ReferenceField(Member)
    final_client = ReferenceField(Company, required=False)

    status = EnumField(MissionStatus, required=True, description="Status of the mission", default=MissionStatus.PENDING)
    application = ReferenceField(Application,required=True)
    meta = {'collection': 'missions'}