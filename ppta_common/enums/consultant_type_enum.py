from enum import Enum


class EnumConsultantType(str, Enum):
    EXTERNAL = 'EXTERNAL'
    INTERNAL = 'INTERNAL'