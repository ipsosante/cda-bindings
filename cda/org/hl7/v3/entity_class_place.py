from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityClassPlace(Enum):
    """specDomain: V10892 (C-0-D10882-V13922-V10892-cpt)"""
    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"
