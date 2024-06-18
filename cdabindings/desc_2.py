from dataclasses import dataclass

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class Desc2:
    class Meta:
        name = "desc"
        namespace = "urn:ihe:pharm:medication"
