from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.struc_doc_col import StrucDocCol
from cda.org.hl7.v3.struc_doc_colgroup_align import StrucDocColgroupAlign
from cda.org.hl7.v3.struc_doc_colgroup_valign import StrucDocColgroupValign

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocColgroup:
    class Meta:
        name = "StrucDoc.Colgroup"

    col: List[StrucDocCol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "styleCode",
            "type": "Attribute",
            "tokens": True,
        }
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[StrucDocColgroupAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[StrucDocColgroupValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
