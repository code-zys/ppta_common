from mongoengine import IntField, StringField, EmbeddedDocumentField, BooleanField, ReferenceField
from .base_document import BaseDocument
from .initial_time_period import InitialTimePeriod
from ..enums.available_period_status_enum import AvailablePeriodStatus

class AvailablePeriod(BaseDocument):
    date = IntField(required=True)
    start_time = IntField(required=True)
    end_time = IntField(required=True)
    timezone = StringField(required=True)
    coach_id = StringField(required=True)
    initial_time_period = EmbeddedDocumentField(InitialTimePeriod, required=False,default=None)
    coaching = ReferenceField('Coaching', required=False, default=None)
    session = ReferenceField('Session', required=False, default=None)
    status = StringField(choices=[e.value for e in AvailablePeriodStatus], required=True)
    reserved_until = IntField(required=False, default=None)
    
    meta = {
        'collection': 'available_periods',
        "strict": False,
        'indexes': [
            {
                'fields': ['coach_id', 'date'],
                'unique': False, 
            },
            'coach_id',
        ]
    }