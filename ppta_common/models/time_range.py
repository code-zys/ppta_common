from mongoengine import StringField, BooleanField, DateField
from ..enums.time_range_type_enum import EnumTimeRangeType
from ..enums.time_range_frequency_enum import FrequencyEnum
from .base_document import BaseDocument

class TimeRange(BaseDocument):
    date = DateField(required=True)
    start_time = DateField(required=True)
    end_time = DateField(required=True)
    timezone = StringField(required=True)
    is_recursive = BooleanField(default=False)
    end_date = DateField(required=False, null=True)
    type = StringField(choices=[e.value for e in EnumTimeRangeType], required=True)
    coach_id = StringField(required=True)
    frequency = StringField(choices=[e.value for e in FrequencyEnum], required=False)