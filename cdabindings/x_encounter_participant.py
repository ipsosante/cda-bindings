from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XEncounterParticipant(Enum):
    ADM = "ADM"
    ATND = "ATND"
    CON = "CON"
    DIS = "DIS"
    REF = "REF"
