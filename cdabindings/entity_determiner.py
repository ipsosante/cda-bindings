from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityDeterminer(Enum):
    INSTANCE = "INSTANCE"
    KIND = "KIND"
    QUANTIFIED_KIND = "QUANTIFIED_KIND"
