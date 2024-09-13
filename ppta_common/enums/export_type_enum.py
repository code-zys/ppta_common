from enum import Enum


class ExportType(str, Enum):
  ATTACHMENT = "ATTACHMENT"
  BODY = "BODY"