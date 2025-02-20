from mongoengine import StringField, ReferenceField, IntField, FloatField
from .member import Member
from .base_document import BaseDocument
from .company import Company
from ..enums.consultant_status_enum import  EnumConsultantStatus
from ..enums.consultant_type_enum import  EnumConsultantType


class Consultant(BaseDocument):
    member = ReferenceField(Member, required=False) # Pour un consutant interne l'objet member n'exite pas à la première invitation
    company = ReferenceField(Company, required=True)
    origin_company = ReferenceField(Company, required=False) # un constultant internet n'a pas de Original company 
    availability_date = IntField(required=False, description="The availability date of the Consultant")
    min_average_daily_rate = FloatField(required=False, min_value=0)
    max_average_daily_rate = FloatField(required=False, min_value=0)
    type= StringField(choices=[e.value for e in EnumConsultantType], required=True)
    status= StringField(choices=[e.value for e in EnumConsultantStatus], required=True)
    invitation_token=StringField(required=False, description="The encripted token that will validate if the invitation is comming from the company")
    email=StringField(required=True, description="The email of the consultant")
    status_date = IntField(required=False)

    meta = {
        "collection": "consultants",
        "strict": False
    }