from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ParticipationTargetLocation(Enum):
    LOC = "LOC"
    DST = "DST"
    ELOC = "ELOC"
    ORG = "ORG"
    RML = "RML"
    VIA = "VIA"
