from mongoengine import StringField, EmbeddedDocument, EnumField

from ..utils.enums import DeliveryRuleModeEnum

class RunDeliveryRule(EmbeddedDocument):
    """
    RunDeliveryRule document
    """
    mode = EnumField(DeliveryRuleModeEnum, default=DeliveryRuleModeEnum.API)
    receiver = StringField()
    receiver_mail = StringField()

    def __str__(self):
        return f"RunDeliveryRule<mode = {self.mode}, receiver = {self.receiver}, receiver_mail = {self.receiver_mail}>"
