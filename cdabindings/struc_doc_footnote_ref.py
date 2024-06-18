from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocFootnoteRef:
    class Meta:
        name = "StrucDoc.FootnoteRef"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        },
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDREF",
            "type": "Attribute",
            "required": True,
        },
    )
