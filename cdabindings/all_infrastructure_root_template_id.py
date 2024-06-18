from dataclasses import dataclass, field

from cdabindings.ii import II

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AllInfrastructureRootTemplateId(II):
    class Meta:
        name = "all.InfrastructureRoot.templateId"

    unsorted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
