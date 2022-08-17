from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityDeterminer(Enum):
    """vocSet: D10878 (C-0-D10878-cpt)"""
    KIND = "KIND"
    QUANTIFIED_KIND = "QUANTIFIED_KIND"
    INSTANCE = "INSTANCE"
