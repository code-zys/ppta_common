from enum import Enum


class ExecutionStatusEnum(str, Enum):
    NOT_STARTED = 'NOT_STARTED'
    IN_PROGESS = 'IN_PROGESS'
    SUCCESSFULLY = 'SUCCESSFULLY'
    FAILED = 'FAILED'