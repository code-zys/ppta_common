import requests

from ..dtos.request.user_dto import UserDtoMetadata

from ..models.notification import Notification, NotificationStatus, NotificationType
from ..dtos.request.notification_dto import NotificationDto
from ..dtos.request.company_dto import CompanyDto
import json
from ..enums.role_enum import EnumRole
from ..utils.utils import Utils
class NotificationService:

    @staticmethod
    def send(url: str, payload: Notification):
        notification:Notification = NotificationService.create(payload)
        
        company_dto:CompanyDto = None
        if notification.to_company:
            company_dto = CompanyDto(
                id=str(notification.to_company.id),
                siren=notification.to_company.siren,
                siret=notification.to_company.siret,
                name=notification.to_company.name,
                activity=notification.to_company.activity,
                type=notification.to_company.type
            )

        notification_dto = NotificationDto(
            id=str(notification.id),
            room=notification.room,
            message=notification.message,
            notification_type=NotificationType(notification.notification_type),
            data=notification.data,
            status=NotificationStatus(notification.status),
            from_user= Utils.construct_user_meta_data(notification.from_user) if notification.from_user else None,
            to_user=Utils.construct_user_meta_data(notification.to_user) if notification.to_user else None,
            to_company=company_dto,
            recipient_roles=[EnumRole(role) for role in notification.recipient_roles]
        )
        
        notification_data:str = json.dumps(notification_dto)

        print('Notificaiton data:: ', notification_data)
        post_result = requests.post(url, data=notification_data)
        print('Post result:: ', post_result)
        return notification_dto


    @staticmethod
    def create(payload: Notification) -> Notification:
        return payload.save()