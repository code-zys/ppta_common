from mongoengine import EmbeddedDocument, StringField, FloatField, DictField, DateTimeField
from ..enums.answer_status_enum import AnswerStatus

class Answer(EmbeddedDocument):
    answer = StringField(required=True)
    ia_matching = FloatField(required=False)
    question = DictField(required=True)
    start_time = DateTimeField(required=False)
    ended_time = DateTimeField(required=False)
    status = StringField(required=True,choices=[e for e in AnswerStatus])