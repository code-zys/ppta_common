from mongoengine import StringField, ReferenceField, IntField, ListField, EmbeddedDocumentField
from .member import Member
from .mission import Mission
from .company import Company
from .timetrack import TimeTrack
from ..enums.timesheet_type_enum import TimesheetType
from ..enums.timesheet_approval_status_enum import TimesheetApprovalStatus
# from ..enums.timesheet_status_enum import TimeSheetStatus
from .base_document import BaseDocument
from ..enums.timesheet_level_enum import TimeSheetLevel
from .consultant import Consultant

class Timesheet(BaseDocument):
    month = IntField(min_value=1, max_value=12, required=True)
    year = StringField(min_value=2000, required=True)
    consultant = ReferenceField(Consultant, required=True)
    mission = ReferenceField(Mission, required=True)
    # function = EmbeddedDocumentField(Function)
    # project = StringField(default=None) #TODO: title of mission by default, can be updated
    # team = StringField(default=None)
    type = StringField(required=True,choices=[e.value for e in TimesheetType],default=TimesheetType.OTHER.value)

    published_by_company = ReferenceField(Company, required=True)
    published_for_company = ReferenceField(Company, required=True)
    supervisor = ReferenceField(Member)

    consultant_observation = StringField(default=None)
    supervisor_observation = StringField(default=None)
    company_observation = StringField(default=None)

    consultant_approved_at = IntField(default=None)
    supervisor_approved_at = IntField(default=None)
    company_approved_at = IntField(default=None)

    # consultant_approval_status = StringField(default=None,choices=[e.value for e in TimesheetApprovalStatus])
    # supervisor_approval_status = StringField(default=None,choices=[e.value for e in TimesheetApprovalStatus])
    # company_approval_status = StringField(default=None,choices=[e.value for e in TimesheetApprovalStatus])

    timetrack = ListField(EmbeddedDocumentField(TimeTrack),default=[])
    status = StringField(required=True, default=TimesheetApprovalStatus.DRAFT.value,choices=[e.value for e in TimesheetApprovalStatus])
    level = StringField(required=True,default=TimeSheetLevel.CONSULTANT.value,choices=[e.value for e in TimeSheetLevel])
    meta = {
            'collection': 'timesheets',
            'strict': False
        }