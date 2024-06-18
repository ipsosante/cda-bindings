from dataclasses import dataclass

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class Id2:
    class Meta:
        name = "id"
        namespace = "urn:ihe:pharm:medication"
