from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XEncounterParticipant(Enum):
    """abstDomain: V19605 (C-0-D10901-V19605-cpt)"""
    ADM = "ADM"
    ATND = "ATND"
    CON = "CON"
    DIS = "DIS"
    REF = "REF"
