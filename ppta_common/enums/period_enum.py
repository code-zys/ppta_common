from enum import Enum


class EnumPeriod(str, Enum):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    YEARLY = 'YEARLY'
    CUSTOM = 'CUSTOM'