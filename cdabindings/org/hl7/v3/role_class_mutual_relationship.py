from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class RoleClassMutualRelationship(Enum):
    """abstDomain: V19316 (C-0-D11555-V13940-V19313-V19316-cpt)"""
    LIC = "LIC"
    NOT = "NOT"
    PROV = "PROV"
    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"
    AGNT = "AGNT"
    GUARD = "GUARD"
    EMP = "EMP"
    MIL = "MIL"
    INVSBJ = "INVSBJ"
    CASESBJ = "CASESBJ"
    RESBJ = "RESBJ"
    CIT = "CIT"
    COVPTY = "COVPTY"
    CRINV = "CRINV"
    CRSPNSR = "CRSPNSR"
    GUAR = "GUAR"
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
