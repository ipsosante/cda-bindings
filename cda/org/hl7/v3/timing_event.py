from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class TimingEvent(Enum):
    """vocSet: D10706 (C-0-D10706-cpt)"""
    AC = "AC"
    ACD = "ACD"
    ACM = "ACM"
    ACV = "ACV"
    HS = "HS"
    IC = "IC"
    ICD = "ICD"
    ICM = "ICM"
    ICV = "ICV"
    PC = "PC"
    PCD = "PCD"
    PCM = "PCM"
    PCV = "PCV"
