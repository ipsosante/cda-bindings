from dataclasses import dataclass, field
from typing import Optional

from cdabindings.struc_doc_col_align import StrucDocColAlign
from cdabindings.struc_doc_col_valign import StrucDocColValign

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocCol:
    class Meta:
        name = "StrucDoc.Col"

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
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[StrucDocColAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[StrucDocColValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
