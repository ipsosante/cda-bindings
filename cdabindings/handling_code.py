from dataclasses import dataclass

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class HandlingCode:
    class Meta:
        name = "handlingCode"
        namespace = "urn:ihe:pharm:medication"
