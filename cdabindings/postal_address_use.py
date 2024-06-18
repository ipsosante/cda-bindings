from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class PostalAddressUse(Enum):
    BAD = "BAD"
    CONF = "CONF"
    DIR = "DIR"
    H = "H"
    HP = "HP"
    HV = "HV"
    PHYS = "PHYS"
    PST = "PST"
    PUB = "PUB"
    TMP = "TMP"
    WP = "WP"
