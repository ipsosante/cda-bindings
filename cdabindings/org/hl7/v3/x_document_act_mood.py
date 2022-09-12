from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XDocumentActMood(Enum):
    """abstDomain: V19458 (C-0-D10196-V19458-cpt)"""
    INT = "INT"
    APT = "APT"
    ARQ = "ARQ"
    DEF = "DEF"
    EVN = "EVN"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"
