from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XRoleClassPayeePolicyRelationship(Enum):
    """abstDomain: V19395 (C-0-D11555-V13940-V19395-cpt)"""
    COVPTY = "COVPTY"
    GUAR = "GUAR"
    POLHOLD = "POLHOLD"
    PROV = "PROV"
    PRS = "PRS"
