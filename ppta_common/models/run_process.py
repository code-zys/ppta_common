from mongoengine import StringField, ListField, BooleanField, \
    DateField, IntField, ReferenceField, EnumField

from base_document import BaseDocument
from utils.enums import FrequencyEnum, ExecutionStatusEnum
from datetime import datetime

from run_invoice_class import RunInvoiceClass
from process_rule import ProcessRule



class RunProcess(BaseDocument):
    """
    RunProcessDocument document
    """
    company_id = StringField()
    plan_cron = StringField()
    name = StringField()
    run_date = DateField(default=datetime.now())
    run_month = IntField()
    run_year = IntField()
    process_rule = ReferenceField(ProcessRule)
    override = BooleanField(default=False)
    run_invoice_classes = ListField(ReferenceField(RunInvoiceClass))
    merge_list = ListField(IntField())
    status = EnumField(ExecutionStatusEnum, required=True)
    frequency = EnumField(FrequencyEnum, required=True)

    meta = {'collection': 'run_process',
            'indexes': ['company_id', 'run_month', 'run_year', 'deleted']
            }

    def __str__(self):
        return f"RunProcess<plan_cron = {self.plan_cron}, name = {self.name}, " \
               f"run_date ={self.run_date}, run_month = {self.run_month}, run_year={self.run_year}, process_rule = {self.process_rule}, status = {self.status}, frequency = {self.frequency}>"