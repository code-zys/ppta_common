from ..utils.enums import EnumRole

class MemberInfo:
    memberId: str
    companyId: str
    userId: str
    role: EnumRole
    
    def __init__(self, companyId: str, userId: str, role: EnumRole, memberId: str):
        self.companyId = companyId
        self.userId = userId
        self.role = role
        self.memberId = memberId
