from pydantic import BaseModel

class AddressDto(BaseModel):
    country: str
    city: str
    street_number: str
    street_name: str
    postal_code: str
