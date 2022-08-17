from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XRoleClassCredentialedEntity(Enum):
    """abstDomain: V16930 (C-0-D11555-V13940-V16930-cpt)"""
    LIC = "LIC"
    NOT = "NOT"
    PROV = "PROV"
    ASSIGNED = "ASSIGNED"
    QUAL = "QUAL"
