from mongoengine import EmbeddedDocument, StringField, FloatField, DictField, DateTimeField
from ..enums.answer_status_enum import AnswerStatus

class Answer(EmbeddedDocument):
    answer = StringField(required=False)
    ia_matching = FloatField(required=False)
    question = DictField(required=True)
    start_time = DateTimeField(required=False)
    end_time = DateTimeField(required=False)
    status = StringField(required=True,choices=[e.value for e in AnswerStatus])