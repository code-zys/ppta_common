from mongoengine import IntField, StringField, EmbeddedDocumentField
from .base_document import BaseDocument
from .initial_time_period import InitialTimePeriod

class AvailablePeriod(BaseDocument):
    date = IntField(required=True)
    start_time = IntField(required=True)
    end_time = IntField(required=True)
    timezone = StringField(required=True)
    coach_id = StringField(required=True)
    initial_time_period = EmbeddedDocumentField(InitialTimePeriod, required=False,default=None)
    
    meta = {
        'collection': 'available_periods',
        "strict": False,
        'indexes': [
            {
                'fields': ['coach_id', 'date'],
                'unique': True 
            },
            'coach_id',
        ]
    }