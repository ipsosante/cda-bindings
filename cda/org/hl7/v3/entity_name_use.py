from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityNameUse(Enum):
    """vocSet: D15913 (C-0-D15913-cpt)"""
    SRCH = "SRCH"
    PHON = "PHON"
    SNDX = "SNDX"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    C = "C"
    L = "L"
    P = "P"
    A = "A"
    ASGN = "ASGN"
    I = "I"
    R = "R"
