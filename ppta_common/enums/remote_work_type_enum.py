from enum import Enum


class RemoteWorkType(Enum):
    FULL_REMOTE = "100% remote"
    PARTIAL_REMOTE = "Partial remote"
    NO_REMOTE = "No remote"