from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityNamePartQualifier(Enum):
    """vocSet: D15888 (C-0-D15888-cpt)"""
    LS = "LS"
    AC = "AC"
    NB = "NB"
    PR = "PR"
    VV = "VV"
    AD = "AD"
    BR = "BR"
    SP = "SP"
    CL = "CL"
    IN = "IN"
    TITLE = "TITLE"
