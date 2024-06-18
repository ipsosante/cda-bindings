from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityNamePartType(Enum):
    DEL = "DEL"
    FAM = "FAM"
    GIV = "GIV"
    PFX = "PFX"
    SFX = "SFX"
