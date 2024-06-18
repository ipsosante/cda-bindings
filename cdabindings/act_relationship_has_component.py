from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipHasComponent(Enum):
    COMP = "COMP"
    ARR = "ARR"
    CTRLV = "CTRLV"
    DEP = "DEP"
