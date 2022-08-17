from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ParticipationPhysicalPerformer(Enum):
    """specDomain: V10248 (C-0-D10901-V10248-cpt)"""
    PRF = "PRF"
    DIST = "DIST"
    PPRF = "PPRF"
    SPRF = "SPRF"
