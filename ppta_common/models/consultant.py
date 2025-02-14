from mongoengine import StringField, ReferenceField, IntField, FloatField
from .member import Member
from .base_document import BaseDocument
from .company import Company
from ..utils.enums import EnumConsultantType, EnumConsultantStatus

class Consultant(BaseDocument):
    member_id = ReferenceField(Member)
    company = ReferenceField(Company)
    origin_company = ReferenceField(Company)
    availability_date = IntField(required=False, description="The availability date of the member")
    min_average_daily_rate = FloatField(required=False, min_value=0)
    max_average_daily_rate = FloatField(required=False, min_value=0)
    type= StringField(choices=[e.value for e in EnumConsultantType], required=True)
    status= StringField(choices=[e.value for e in EnumConsultantStatus], required=True)

    meta = {
        "collection": "consultants",
        "strict": False
    }