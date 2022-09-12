from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipOutcome(Enum):
    """specDomain: V10324 (C-0-D10317-V10324-cpt)"""
    OBJC = "OBJC"
    OBJF = "OBJF"
    OUTC = "OUTC"
    GOAL = "GOAL"
    RISK = "RISK"
