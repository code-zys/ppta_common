from mongoengine import StringField, ReferenceField, IntField, FloatField
from .member import Member
from .base_document import BaseDocument
from .company import Company
from ..enums.consultant_status_enum import  EnumConsultantStatus
from ..enums.consultant_type_enum import  EnumConsultantType


class Consultant(BaseDocument):
    member = ReferenceField(Member, required=True)
    company = ReferenceField(Company, required=True)
    origin_company = ReferenceField(Company, required=True)
    availability_date = IntField(required=False, description="The availability date of the member")
    min_average_daily_rate = FloatField(required=False, min_value=0)
    max_average_daily_rate = FloatField(required=False, min_value=0)
    type= StringField(choices=[e.value for e in EnumConsultantType], required=True)
    status= StringField(choices=[e.value for e in EnumConsultantStatus], required=True)

    meta = {
        "collection": "consultants",
        "strict": False
    }