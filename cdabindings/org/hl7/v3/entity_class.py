from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityClass(Enum):
    """vocSet: D10882 (C-0-D10882-cpt)"""
    NLIV = "NLIV"
    ANM = "ANM"
    MIC = "MIC"
    PLNT = "PLNT"
    LIV = "LIV"
    PSN = "PSN"
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"
    MAT = "MAT"
    CHEM = "CHEM"
    FOOD = "FOOD"
    STATE = "STATE"
    NAT = "NAT"
    ORG = "ORG"
    PUB = "PUB"
    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"
    ENT = "ENT"
    HCE = "HCE"
    RGRP = "RGRP"
