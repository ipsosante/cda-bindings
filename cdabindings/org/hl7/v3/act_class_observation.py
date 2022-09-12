from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActClassObservation(Enum):
    """specDomain: V11529 (C-0-D11527-V13856-V11529-cpt)"""
    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"
    OBS = "OBS"
    ALRT = "ALRT"
    CLNTRL = "CLNTRL"
    CNOD = "CNOD"
    DGIMG = "DGIMG"
    INVSTG = "INVSTG"
    SPCOBS = "SPCOBS"
