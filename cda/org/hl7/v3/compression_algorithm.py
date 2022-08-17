from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class CompressionAlgorithm(Enum):
    """vocSet: D10620 (C-0-D10620-cpt)"""
    DF = "DF"
    GZ = "GZ"
    Z = "Z"
    ZL = "ZL"
