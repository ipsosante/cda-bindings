from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class IntegrityCheckAlgorithm(Enum):
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"
