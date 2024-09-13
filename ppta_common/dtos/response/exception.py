
from .enum_response import EnumStatusCode


class GenericException(Exception):
    statusCode: EnumStatusCode
    message: str

    def __init__(self, statusCode, message):
        self.statusCode = statusCode
        self.message = message

