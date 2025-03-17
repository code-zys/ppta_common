import requests


from ..models.notification import Notification
from ..dtos.request.notification_dto import NotificationDto
from ..dtos.request.company_dto import CompanyDto
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
                siret=notification.to_company.siret,
                name=notification.to_company.name,
                activity=notification.to_company.activity,
                type=notification.to_company.type
            )

        notification_dto = NotificationDto(
            id=str(notification.id),
            room=notification.room,
            message=notification.message,
            notification_type=notification.notification_type,
            data=notification.data,
            status=notification.status,
            from_user= Utils.construct_user_meta_data_dto(notification.from_user) if notification.from_user else None,
            to_user=Utils.construct_user_meta_data_dto(notification.to_user) if notification.to_user else None,
            to_company=company_dto,
            recipient_roles=[EnumRole(role) for role in notification.recipient_roles],
            created_at=notification.created_at
        )
        
        notification_data:str = notification_dto.model_dump_json()

        print('Notificaiton data:: ', notification_data)
        post_result = requests.post(url, data=notification_data, verify=False)
        print('Post result:: ', post_result)
        return notification_dto


    @staticmethod
    def create(payload: Notification) -> Notification:
        return payload.save()