from enum import Enum


class ConnectionCategoryEnum(Enum):
    PUSH = 'PUSH'
    PULL = 'PULL'
    DISTRIBUTION = 'DISTRIBUTION'