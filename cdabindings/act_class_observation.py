from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActClassObservation(Enum):
    OBS = "OBS"
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SFWL = "SFWL"
    SIT = "SIT"
    STN = "STN"
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    ALRT = "ALRT"
    BATTERY = "BATTERY"
    CLNTRL = "CLNTRL"
    CNOD = "CNOD"
    CONC = "CONC"
    COND = "COND"
    CASE = "CASE"
    OUTB = "OUTB"
    DGIMG = "DGIMG"
    GEN = "GEN"
    DETPOL = "DETPOL"
    EXP = "EXP"
    LOC = "LOC"
    PHN = "PHN"
    POL = "POL"
    SEQ = "SEQ"
    SEQVAR = "SEQVAR"
    INVSTG = "INVSTG"
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"
    SPCOBS = "SPCOBS"
    VERIF = "VERIF"
