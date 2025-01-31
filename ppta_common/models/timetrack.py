from mongoengine import EmbeddedDocument, IntField, ReferenceField
from ..enums.work_type_enum import WorkType

class TimeTrack(EmbeddedDocument):
    day = IntField(min_value=1, max_value=31, required=True)
    duration = IntField(required=True, max_value=1, min_value=0)
    work_type = ReferenceField(WorkType, required=True)