from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XActRelationshipPertinentInfo(Enum):
    """abstDomain: V19562 (C-0-D10317-V19562-cpt)"""
    SPRT = "SPRT"
    CAUS = "CAUS"
    MFST = "MFST"
    REFR = "REFR"
    SUBJ = "SUBJ"
