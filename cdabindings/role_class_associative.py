from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class RoleClassAssociative(Enum):
    AFFL = "AFFL"
    AGNT = "AGNT"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    GUARD = "GUARD"
    CIT = "CIT"
    COVPTY = "COVPTY"
    CLAIM = "CLAIM"
    NAMED = "NAMED"
    DEPEN = "DEPEN"
    INDIV = "INDIV"
    SUBSCR = "SUBSCR"
    PROG = "PROG"
    CRINV = "CRINV"
    CRSPNSR = "CRSPNSR"
    EMP = "EMP"
    MIL = "MIL"
    GUAR = "GUAR"
    INVSBJ = "INVSBJ"
    CASEBJ = "CASEBJ"
    RESBJ = "RESBJ"
    LIC = "LIC"
    NOT = "NOT"
    PROV = "PROV"
    PAT = "PAT"
    PAYEE = "PAYEE"
    PAYOR = "PAYOR"
    POLHOLD = "POLHOLD"
    QUAL = "QUAL"
    SPNSR = "SPNSR"
    STD = "STD"
    UNDWRT = "UNDWRT"
    CAREGIVER = "CAREGIVER"
    PRS = "PRS"
    ACCESS = "ACCESS"
    ADJY = "ADJY"
    CONC = "CONC"
    BOND = "BOND"
    CONY = "CONY"
    ADMM = "ADMM"
    BIRTHPL = "BIRTHPL"
    DEATHPLC = "DEATHPLC"
    DST = "DST"
    RET = "RET"
    EXPR = "EXPR"
    HLD = "HLD"
    HLTHCHRT = "HLTHCHRT"
    IDENT = "IDENT"
    MANU = "MANU"
    THER = "THER"
    MNT = "MNT"
    OWN = "OWN"
    RGPR = "RGPR"
    SDLOC = "SDLOC"
    DSDLOC = "DSDLOC"
    ISDLOC = "ISDLOC"
    TERR = "TERR"
    USED = "USED"
    WRTE = "WRTE"
