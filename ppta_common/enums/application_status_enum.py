from enum import Enum

class ApplicationStatus(Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"
    INVITED = "INVITED"
    QUESTION_ANSWERED = "QUESTION_ANSWERED"
    SELECTED = "SELECTED"