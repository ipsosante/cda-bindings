from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityClassOrganization(Enum):
    """specDomain: V10889 (C-0-D10882-V19463-V10889-cpt)"""
    STATE = "STATE"
    NAT = "NAT"
    ORG = "ORG"
    PUB = "PUB"
