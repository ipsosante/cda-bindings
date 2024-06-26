from dataclasses import dataclass, field
from typing import Optional

from cdabindings.struc_doc_br import StrucDocBr
from cdabindings.struc_doc_caption import (
    StrucDocContent,
    StrucDocFootnote,
    StrucDocLinkHtml,
    StrucDocList,
    StrucDocParagraph,
    StrucDocRenderMultiMedia,
    StrucDocTable,
)
from cdabindings.struc_doc_footnote_ref import StrucDocFootnoteRef
from cdabindings.struc_doc_sub import StrucDocSub
from cdabindings.struc_doc_sup import StrucDocSup

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocText:
    class Meta:
        name = "StrucDoc.Text"

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
    media_type: str = field(
        init=False,
        default="text/x-hl7-text+xml",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "content",
                    "type": StrucDocContent,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": StrucDocLinkHtml,
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
                    "type": StrucDocBr,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnote",
                    "type": StrucDocFootnote,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "paragraph",
                    "type": StrucDocParagraph,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "list",
                    "type": StrucDocList,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "table",
                    "type": StrucDocTable,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )
