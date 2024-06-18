from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class EntityClassPlace(Enum):
    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"
