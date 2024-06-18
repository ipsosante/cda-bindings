from dataclasses import dataclass

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class RiskCode:
    class Meta:
        name = "riskCode"
        namespace = "urn:ihe:pharm:medication"
