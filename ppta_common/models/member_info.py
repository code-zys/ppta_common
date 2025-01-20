from ..utils.enums import EnumRole

class MemberInfo:
    memberId: str
    companyId: str
    userId: str
    role: EnumRole
    is_consultant: bool
    is_commercial: bool
    
    def __init__(self, companyId: str, userId: str, role: EnumRole, memberId: str, is_consultant: bool = False, is_commercial: bool = False):
        self.companyId = companyId
        self.userId = userId
        self.role = role
        self.memberId = memberId
        self.is_consultant = is_consultant
        self.is_commercial = is_commercial
