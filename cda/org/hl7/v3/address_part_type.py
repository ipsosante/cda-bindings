from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class AddressPartType(Enum):
    """vocSet: D10642 (C-0-D10642-cpt)"""
    ADL = "ADL"
    UNID = "UNID"
    UNIT = "UNIT"
    DAL = "DAL"
    DINST = "DINST"
    DINSTA = "DINSTA"
    DINSTQ = "DINSTQ"
    DMOD = "DMOD"
    DMODID = "DMODID"
    BNR = "BNR"
    BNN = "BNN"
    BNS = "BNS"
    STR = "STR"
    STB = "STB"
    STTYP = "STTYP"
    SAL = "SAL"
    DIR = "DIR"
    CAR = "CAR"
    CEN = "CEN"
    CNT = "CNT"
    CPA = "CPA"
    CTY = "CTY"
    DEL = "DEL"
    POB = "POB"
    PRE = "PRE"
    STA = "STA"
    ZIP = "ZIP"
