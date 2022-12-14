from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActClassRoot(Enum):
    """specDomain: V13856 (C-0-D11527-V13856-cpt)"""
    FCNTRCT = "FCNTRCT"
    COV = "COV"
    CNTRCT = "CNTRCT"
    CACT = "CACT"
    ACTN = "ACTN"
    INFO = "INFO"
    STC = "STC"
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
    SPLY = "SPLY"
    DIET = "DIET"
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"
    COMPOSITION = "COMPOSITION"
    ENTRY = "ENTRY"
    BATTERY = "BATTERY"
    CLUSTER = "CLUSTER"
    EXTRACT = "EXTRACT"
    EHR = "EHR"
    ORGANIZER = "ORGANIZER"
    CATEGORY = "CATEGORY"
    DOCBODY = "DOCBODY"
    DOCSECT = "DOCSECT"
    TOPIC = "TOPIC"
    FOLDER = "FOLDER"
    ACT = "ACT"
    ACCM = "ACCM"
    CONS = "CONS"
    CTTEVENT = "CTTEVENT"
    INC = "INC"
    INFRM = "INFRM"
    PCPR = "PCPR"
    REG = "REG"
    SPCTRT = "SPCTRT"
    ACCT = "ACCT"
    ACSN = "ACSN"
    ADJUD = "ADJUD"
    CONTREG = "CONTREG"
    DISPACT = "DISPACT"
    ENC = "ENC"
    INVE = "INVE"
    LIST = "LIST"
    MPROT = "MPROT"
    PROC = "PROC"
    REV = "REV"
    SBADM = "SBADM"
    SUBST = "SUBST"
    TRNS = "TRNS"
    VERIF = "VERIF"
    XACT = "XACT"
