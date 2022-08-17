from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipFulfills(Enum):
    """specDomain: V10342 (C-0-D10317-V10337-V10342-cpt)"""
    FLFS = "FLFS"
    OCCR = "OCCR"
    OREF = "OREF"
    SCH = "SCH"
