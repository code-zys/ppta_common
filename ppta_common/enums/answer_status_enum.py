from enum import Enum

class AnswerStatus(Enum):
    TIMEOUT = "TIMEOUT"
    PENDING = "PENDING"
    ANSWERED = "ANSWERED"
    INITIAL = "INITIAL"