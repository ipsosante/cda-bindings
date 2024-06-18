from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ContextControl(Enum):
    AN = "AN"
    AP = "AP"
    ON = "ON"
    OP = "OP"
