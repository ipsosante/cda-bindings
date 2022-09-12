from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.v3.struc_doc_footnote_ref import StrucDocFootnoteRef
from cdabindings.org.hl7.v3.struc_doc_sub import StrucDocSub
from cdabindings.org.hl7.v3.struc_doc_sup import StrucDocSup
from cdabindings.org.hl7.v3.struc_doc_title_footnote import (
    StrucDocTitleContent,
    StrucDocTitleFootnote,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocTitle:
    class Meta:
        name = "StrucDoc.Title"

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
    media_type: str = field(
        init=False,
        default="text/x-hl7-title+xml",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "content",
                    "type": StrucDocTitleContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sub",
                    "type": StrucDocSub,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "sup",
                    "type": StrucDocSup,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "br",
                    "type": str,
                    "namespace": "urn:hl7-org:v3",
                    "max_length": 0,
                },
                {
                    "name": "footnote",
                    "type": StrucDocTitleFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        }
    )
