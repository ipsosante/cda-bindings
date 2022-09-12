from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipPosting(Enum):
    """abstDomain: V19617 (C-0-D10317-V10329-V14900-V19617-cpt)"""
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
