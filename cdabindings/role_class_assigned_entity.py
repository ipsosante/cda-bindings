from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class RoleClassAssignedEntity(Enum):
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    SGNOFF = "SGNOFF"
