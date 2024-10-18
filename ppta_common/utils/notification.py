import requests
from ..models.notification import Notification
import json

class NotificationService:

    @staticmethod
    def send(url: str, payload: Notification):
        result = NotificationService.create(payload)
        requests.post(url, data=json.dumps(result.to_dict()))
        return result


    @staticmethod
    def create(payload: Notification) -> Notification:
        return payload.save()