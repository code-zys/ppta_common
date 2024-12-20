from enum import Enum


class EnumPaymentStatus(str, Enum):
    NOT_COMPLETE = 'NOT_COMPLETE'
    COMPLETED = 'COMPLETED'
    IN_PROGRESS = 'IN_PROGRESS'
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'