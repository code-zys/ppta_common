from mongoengine import Document, StringField, ReferenceField, IntField, ListField, EmbeddedDocumentField
from .member import Member
from .mission import Mission
from .function import Function
from .company import Company
from .timetrack import TimeTrack
from ..enums.timesheet_type_enum import TimesheetType
from ..enums.timesheet_approval_status_enum import TimesheetApprovalStatus
from ..enums.timesheet_status_enum import TimeSheetStatus

class Timesheet(Document):
    month = IntField(min_value=1, max_value=12, required=True)
    year = StringField(min_value=2000, required=True)
    member = ReferenceField(Member, required=True)
    mission = ReferenceField(Mission, required=True)
    function = ReferenceField(Function)
    project = StringField() #TODO: title of mission by default, can be updated
    team = StringField()
    type = ReferenceField(TimesheetType, required=True)

    published_by_company = ReferenceField(Company, required=True)
    published_for_company = ReferenceField(Company, required=True)
    supervisor_member = ReferenceField(Member)

    member_observation = StringField()
    supervisor_observation = StringField()
    company_observation = StringField()

    member_approved_at = IntField()
    supervisor_approved_at = IntField()
    company_approved_at = IntField()

    member_approval_status = ReferenceField(TimesheetApprovalStatus)
    supervisor_approval_status = ReferenceField(TimesheetApprovalStatus)
    company_approval_status = ReferenceField(TimesheetApprovalStatus)

    timetrack = ListField(EmbeddedDocumentField(TimeTrack))
    status = StringField(required=True, default=TimeSheetStatus.DRAFT.value,choices=[e.value for e in TimeSheetStatus])
    meta = {
            'collection': 'timesheets',
            'strict': False
        }