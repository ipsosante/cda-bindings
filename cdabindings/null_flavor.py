from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class NullFlavor(Enum):
    ASKU = "ASKU"
    DER = "DER"
    INV = "INV"
    MSK = "MSK"
    NA = "NA"
    NASK = "NASK"
    NAV = "NAV"
    NI = "NI"
    NINF = "NINF"
    OTH = "OTH"
    PINF = "PINF"
    QS = "QS"
    TRC = "TRC"
    UNC = "UNC"
    UNK = "UNK"
