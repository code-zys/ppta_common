from enum import Enum


class TenderCallStatus(Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"
    CLOSED = "CLOSED"