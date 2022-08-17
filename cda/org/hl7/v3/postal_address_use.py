from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class PostalAddressUse(Enum):
    """vocSet: D10637 (C-0-D10637-cpt)"""
    H = "H"
    HP = "HP"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    TMP = "TMP"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    PHYS = "PHYS"
    PST = "PST"
