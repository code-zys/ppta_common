from typing import Dict, Optional
from .extended_base_model import ExtendedBaseModel
from ...models.notification import NotificationType, NotificationStatus
from typing import Optional, List, Dict
from ...enums.role_enum import EnumRole
from .user_dto import UserDtoMetadata
from .company_dto import CompanyDto

class NotificationDto(ExtendedBaseModel):
    id: Optional[str] = None
    room: str
    message: str
    notification_type: NotificationType
    data: Optional[Dict] = {}
    status: NotificationStatus = NotificationStatus.UNREAD
    from_user: Optional[UserDtoMetadata] = None
    to_user: Optional[UserDtoMetadata] = None
    to_company: Optional[CompanyDto] = None
    recipient_roles: List[EnumRole] = []
