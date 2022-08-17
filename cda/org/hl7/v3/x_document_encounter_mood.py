from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XDocumentEncounterMood(Enum):
    """abstDomain: V19459 (C-0-D10196-V19459-cpt)"""
    INT = "INT"
    APT = "APT"
    ARQ = "ARQ"
    EVN = "EVN"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"
