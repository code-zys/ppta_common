import requests
from ..models.notification import Notification
import json

class NotificationService:

    @staticmethod
    def send(url: str, payload: Notification):
        result = NotificationService.create(payload)
        notification_data:str = json.dumps(result.to_dict())
        print('Notificaiton data:: ', notification_data)
        post_result = requests.post(url, data=notification_data)
        print('Post result:: ', post_result)
        return result


    @staticmethod
    def create(payload: Notification) -> Notification:
        return payload.save()