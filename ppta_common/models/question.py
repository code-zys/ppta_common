from ..enums.question_difficulty_enum import QuestionDifficulty
from mongoengine import EmbeddedDocument, StringField, IntField

class Question(EmbeddedDocument):
    title = StringField(required=True, description="The text of the question")
    time = IntField(required=True, description="Time allocated for the question in minutes", min_value=0)
    difficulty = StringField(required=True, choices=[choice.value for choice in QuestionDifficulty], description="Difficulty level of the question")