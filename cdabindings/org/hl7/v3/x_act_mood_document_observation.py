from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XActMoodDocumentObservation(Enum):
    """abstDomain: V18943 (C-0-D10196-V18943-cpt)"""
    INT = "INT"
    DEF = "DEF"
    EVN = "EVN"
    GOL = "GOL"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"
