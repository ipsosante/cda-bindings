from dataclasses import dataclass

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class StabilityTime:
    class Meta:
        name = "stabilityTime"
        namespace = "urn:ihe:pharm:medication"
