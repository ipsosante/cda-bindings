from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class TimingEvent(Enum):
    AC = "AC"
    ACD = "ACD"
    ACM = "ACM"
    ACV = "ACV"
    C = "C"
    CD = "CD"
    CM = "CM"
    CV = "CV"
    HS = "HS"
    IC = "IC"
    ICD = "ICD"
    ICM = "ICM"
    ICV = "ICV"
    PC = "PC"
    PCD = "PCD"
    PCM = "PCM"
    PCV = "PCV"
    WAKE = "WAKE"
