from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityClassManufacturedMaterial(Enum):
    MMAT = "MMAT"
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
