from dataclasses import dataclass

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class ExpirationTime:
    class Meta:
        name = "expirationTime"
        namespace = "urn:ihe:pharm:medication"
