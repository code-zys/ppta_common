from fastapi import HTTPException


class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Not Found"):
        super().__init__(status_code=404, detail=detail)


class PaginationException(HTTPException):
    def __init__(self, detail: str = "Bad pagination params"):
        super().__init__(status_code=400, detail=detail)
