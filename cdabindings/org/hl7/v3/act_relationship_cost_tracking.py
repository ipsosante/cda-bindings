from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipCostTracking(Enum):
    """abstDomain: V19618 (C-0-D10317-V10329-V14900-V19618-cpt)"""
    CHRG = "CHRG"
    COST = "COST"
