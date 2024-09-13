
from pydantic import BaseModel, Field
from professional_info_dto import ProfessionalInfoDto
from utils.enums import EnumUserType

class UserDto(BaseModel):
    professional_info: ProfessionalInfoDto
    user_type:EnumUserType
    company_id: str

class UserDtoMetadata(BaseModel):
    id: str = Field(..., alias='_id')
    email: str
    firstname: str
    lastname: str
    enabled: bool
    disabledByAdmin: bool
    userId: str