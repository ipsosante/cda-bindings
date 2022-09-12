from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class RoleClassAssignedEntity(Enum):
    """specDomain: V11595 (C-0-D11555-V13940-V19313-V19316-V10416-V14006-V11595-cpt)"""
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"
