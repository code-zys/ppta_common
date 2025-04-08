from mongoengine import  StringField, ListField, BooleanField, IntField, EmbeddedDocumentField, ReferenceField, FloatField
from .address import Address
from .language import Language
from .skill import Skill
from .base_document import BaseDocument
from .company import Company
from .workplace import Workplace


class Coach(BaseDocument):
    """
    Coach model
    """
    name = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    phone = StringField(max_length=50, required=True)
    languages = ListField(EmbeddedDocumentField('Language'), required=False)
    min_booking_time = IntField(required=False)
    workplaces = ListField(EmbeddedDocumentField('Workplace'), required=False) 
    member_id = StringField(required=False)
    is_coaching_profile_visible = BooleanField(default=True)
    is_profile_verified= BooleanField(default=False)
    is_profile_disabled_by_admin = BooleanField(default=False)
    company_approved_coach = BooleanField(default=True)
    company = ReferenceField(Company, required=True)
    bio = StringField(required=False)
    profile_picture = StringField(required=False)
    slug = StringField(required=False)
    address = EmbeddedDocumentField(Address, required=False)
    skills = ListField(EmbeddedDocumentField(Skill), required=False)
    hourly_rate = FloatField(required=False)
    price_id = StringField(required=True)
    
    meta = {
        'indexes': [
            'slug',  
            'member_id',  
        ]
    }