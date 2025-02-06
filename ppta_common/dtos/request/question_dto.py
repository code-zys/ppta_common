from pydantic import BaseModel, Field
from ...enums.question_difficulty_enum import QuestionDifficulty

class QuestionDto(BaseModel):
    title: str = Field(..., description="The text of the question")
    time: int = Field(..., description="Time allocated for the question in minutes")
    difficulty: QuestionDifficulty = Field(..., description="Difficulty level of the question")
