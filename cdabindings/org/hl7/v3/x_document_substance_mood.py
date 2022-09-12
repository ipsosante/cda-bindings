from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XDocumentSubstanceMood(Enum):
    """abstDomain: V19461 (C-0-D10196-V19461-cpt)"""
    INT = "INT"
    EVN = "EVN"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"
