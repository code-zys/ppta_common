from mongoengine import StringField, ListField, BooleanField, \
    DateField, IntField

from .base_document import BaseDocument
from utils.enums import FrequencyEnum

class ProcessRule(BaseDocument):
    """
    ProcessRule document
    """
    company_id = StringField()
    plan_cron = StringField() # permet uniquement de déterminer le next_execution_date
    next_execution_date = DateField(required = False, default=None) 
    run_day = StringField() # permet de definir le jour pour une exécution mensuelle et annuelle et donc fabriquer le cron
    run_month = IntField() # permet de definir le jour pour une exécution annuelle et sert à fabriquer le cron
    next_year = IntField(required = True) # next_year et next_month permettent de déterminer pour quelle periode la collecte est faite
    next_month = IntField()
    frequency = StringField(choices=[e.value for e in FrequencyEnum], required=True)
    name = StringField()
    invoice_class_ids = ListField(StringField())
    all_invoice = BooleanField(default=False)
    enabled = BooleanField(default=True)
    override = BooleanField()
    meta = {'collection': 'process_rule',
            'indexes': [
                'company_id', 'deleted'  # Index on the company_id field
            ]
            }

    def __str__(self):
        return f"ProcessRule<company_id = {self.company_id}, plan_cron = {self.plan_cron}, " \
               f"name = {self.name}, next_execution_date = {self.next_execution_date}, override = {self.override}," \
               f"invoice_class_ids ={self.invoice_class_ids}, all_invoice = {self.all_invoice}>"
