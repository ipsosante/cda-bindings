from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XActClassDocumentEntryAct(Enum):
    """abstDomain: V19604 (C-0-D11527-V13856-V19604-cpt)"""
    ACT = "ACT"
    ACCM = "ACCM"
    CONS = "CONS"
    CTTEVENT = "CTTEVENT"
    INC = "INC"
    INFRM = "INFRM"
    PCPR = "PCPR"
    REG = "REG"
    SPCTRT = "SPCTRT"
