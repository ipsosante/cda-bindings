from dataclasses import dataclass, field

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocSup:
    class Meta:
        name = "StrucDoc.Sup"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
