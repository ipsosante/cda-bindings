from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipConditional(Enum):
    """abstDomain: V18977 (C-0-D10317-V18977-cpt)"""
    RSON = "RSON"
    MITGT = "MITGT"
    CIND = "CIND"
    PRCN = "PRCN"
    TRIG = "TRIG"
