from enum import Enum

class MissionStatus(Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"
    # IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"