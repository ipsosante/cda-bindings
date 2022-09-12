from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipHasComponent(Enum):
    """specDomain: V10318 (C-0-D10317-V10318-cpt)"""
    COMP = "COMP"
    ARR = "ARR"
    CTRLV = "CTRLV"
    DEP = "DEP"
