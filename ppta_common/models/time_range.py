from mongoengine import EmbeddedDocument, StringField, BooleanField
from ..enums.time_range_type import EnumTimeRangeType

class TimeRange(EmbeddedDocument):
    date = StringField(required=True)
    start_time = StringField(required=True)
    end_time = StringField(required=True)
    timezone = StringField(required=True)
    is_recursive = BooleanField(default=False)
    end_date = StringField(required=False, null=True)
    type = StringField(choices=[e.value for e in EnumTimeRangeType], required=True)
    coach_id = StringField(required=True)