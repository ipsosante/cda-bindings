from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class NullFlavor(Enum):
    """vocSet: D10609 (C-0-D10609-cpt)"""
    OTH = "OTH"
    NINF = "NINF"
    PINF = "PINF"
    ASKU = "ASKU"
    NAV = "NAV"
    UNK = "UNK"
    NASK = "NASK"
    TRC = "TRC"
    NI = "NI"
    MSK = "MSK"
    NA = "NA"
    NP = "NP"
