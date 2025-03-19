from mongoengine import EmbeddedDocument, IntField

class TotalDays(EmbeddedDocument):
    work_days = IntField(required=True, default=0)
    paid_leave = IntField(required=True, default=0)
    days_off = IntField(required=True, default=0)