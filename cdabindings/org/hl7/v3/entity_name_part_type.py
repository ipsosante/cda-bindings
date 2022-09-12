from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityNamePartType(Enum):
    """vocSet: D15880 (C-0-D15880-cpt)"""
    DEL = "DEL"
    PFX = "PFX"
    SFX = "SFX"
    FAM = "FAM"
    GIV = "GIV"
