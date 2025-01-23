from mongoengine import StringField, FloatField, ListField, IntField
from .base_document import BaseDocument

class ExonerationNature(BaseDocument):
    code = StringField(required=True, default="", help_text="Code unique de l'exonération")
    description = StringField(required=True, default="", help_text="Description de l'exonération")
    label = StringField(required=False, help_text="Libellé de l'exonération")
    rate = FloatField(required=False, default=0.0, help_text="Taux d'exonération applicable")
    conditions = StringField(required=False, help_text="Conditions d'éligibilité à l'exonération")
    scope = StringField(required=False, help_text="Champ d'application de l'exonération (ex: secteur, type d'opération)")
    eligibility_criteria = ListField(StringField(), required=False, help_text="Critères d'éligibilité pour bénéficier de l'exonération")
    applicable_thresholds = ListField(FloatField(), required=False, help_text="Seuils applicables pour bénéficier de l'exonération")
    duration = IntField(required=False, help_text="Durée pendant laquelle l'exonération est applicable")
    exclusions = StringField(required=False, help_text="Exceptions ou exclusions de l'exonération")
    notes = StringField(required=False, help_text="Notes supplémentaires sur l'exonération")
    meta = {
        'collection': 'exoneration_natures',
        "strict": False
    }