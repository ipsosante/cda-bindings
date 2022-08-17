from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityClassManufacturedMaterial(Enum):
    """specDomain: V13934 (C-0-D10882-V13922-V10883-V13934-cpt)"""
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"
