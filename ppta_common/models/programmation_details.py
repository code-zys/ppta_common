from mongoengine import DateField, StringField, IntField, EmbeddedDocument
from ..enums.period_enum import EnumPeriod
from ..enums.custom_frequency_enum import EnumCustomFrequency

class Programmation_details(EmbeddedDocument):
    starting_date =DateField(required=True, default=None)
    frequency = StringField(choices=[e.value for e in EnumPeriod], required=False)
    custom_frequency = IntField(required=False, default=None)
    custom_frequency_unit = StringField(choices=[e.value for e in EnumCustomFrequency], required=False)
    ending_date = DateField(required=False, default=None)