from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class CompressionAlgorithm(Enum):
    DF = "DF"
    GZ = "GZ"
    Z = "Z"
    ZL = "ZL"
