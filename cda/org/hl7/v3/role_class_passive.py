from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class RoleClassPassive(Enum):
    """abstDomain: V19105 (C-0-D11555-V13940-V19313-V19105-cpt)"""
    DST = "DST"
    RET = "RET"
    MANU = "MANU"
    THER = "THER"
    SDLOC = "SDLOC"
    DSDLOC = "DSDLOC"
    ISDLOC = "ISDLOC"
    ACCESS = "ACCESS"
    BIRTHPL = "BIRTHPL"
    EXPR = "EXPR"
    HLD = "HLD"
    HLTHCHRT = "HLTHCHRT"
    IDENT = "IDENT"
    MNT = "MNT"
    OWN = "OWN"
    RGPR = "RGPR"
    TERR = "TERR"
    WRTE = "WRTE"
