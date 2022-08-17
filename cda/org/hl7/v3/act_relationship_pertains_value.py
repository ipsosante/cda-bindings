from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipPertainsValue(Enum):
    PERT = "PERT"
    AUTH = "AUTH"
    CAUS = "CAUS"
    COVBY = "COVBY"
    DRIV = "DRIV"
    EXPL = "EXPL"
    ITEMSLOC = "ITEMSLOC"
    LIMIT = "LIMIT"
    MFST = "MFST"
    NAME = "NAME"
    PREV = "PREV"
    REFR = "REFR"
    REFV = "REFV"
    SUBJ = "SUBJ"
    SUMM = "SUMM"
