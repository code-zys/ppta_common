import requests
from ..models.notification import Notification

class NotificationService:

    @staticmethod
    def send(url: str, payload: Notification):
        result = NotificationService.create(payload)
        requests.post(url, data=result)
        return result


    @staticmethod
    def create(payload: Notification):
        return Notification.save(payload)