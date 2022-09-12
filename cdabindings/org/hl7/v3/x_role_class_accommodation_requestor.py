from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XRoleClassAccommodationRequestor(Enum):
    """abstDomain: V19382 (C-0-D11555-V13940-V19382-cpt)"""
    AGNT = "AGNT"
    PAT = "PAT"
    PROV = "PROV"
    PRS = "PRS"
