from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ContextControl(Enum):
    """vocSet: D16478 (C-0-D16478-cpt)"""
    AN = "AN"
    AP = "AP"
    ON = "ON"
    OP = "OP"
