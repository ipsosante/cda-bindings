from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ParticipationTargetLocation(Enum):
    """specDomain: V10302 (C-0-D10901-V10302-cpt)"""
    LOC = "LOC"
    DST = "DST"
    ELOC = "ELOC"
    ORG = "ORG"
    RML = "RML"
    VIA = "VIA"
