from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XDocumentProcedureMood(Enum):
    """abstDomain: V19460 (C-0-D10196-V19460-cpt)"""
    INT = "INT"
    APT = "APT"
    ARQ = "ARQ"
    DEF = "DEF"
    EVN = "EVN"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"
