from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class TelecommunicationAddressUse(Enum):
    """vocSet: D201 (C-0-D201-cpt)"""
    H = "H"
    HP = "HP"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    TMP = "TMP"
    AS = "AS"
    EC = "EC"
    MC = "MC"
    PG = "PG"
