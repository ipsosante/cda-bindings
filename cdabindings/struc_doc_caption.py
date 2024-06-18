from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from cdabindings.struc_doc_br import StrucDocBr
from cdabindings.struc_doc_col import StrucDocCol
from cdabindings.struc_doc_colgroup import StrucDocColgroup
from cdabindings.struc_doc_content_revised import StrucDocContentRevised
from cdabindings.struc_doc_footnote_ref import StrucDocFootnoteRef
from cdabindings.struc_doc_list_list_type import StrucDocListListType
from cdabindings.struc_doc_sub import StrucDocSub
from cdabindings.struc_doc_sup import StrucDocSup
from cdabindings.struc_doc_table_frame import StrucDocTableFrame
from cdabindings.struc_doc_table_rules import StrucDocTableRules
from cdabindings.struc_doc_tbody_align import StrucDocTbodyAlign
from cdabindings.struc_doc_tbody_valign import StrucDocTbodyValign
from cdabindings.struc_doc_td_align import StrucDocTdAlign
from cdabindings.struc_doc_td_scope import StrucDocTdScope
from cdabindings.struc_doc_td_valign import StrucDocTdValign
from cdabindings.struc_doc_tfoot_align import StrucDocTfootAlign
from cdabindings.struc_doc_tfoot_valign import StrucDocTfootValign
from cdabindings.struc_doc_th_align import StrucDocThAlign
from cdabindings.struc_doc_th_scope import StrucDocThScope
from cdabindings.struc_doc_th_valign import StrucDocThValign
from cdabindings.struc_doc_thead_align import StrucDocTheadAlign
from cdabindings.struc_doc_thead_valign import StrucDocTheadValign
from cdabindings.struc_doc_tr_align import StrucDocTrAlign
from cdabindings.struc_doc_tr_valign import StrucDocTrValign

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocCaption:
    class Meta:
        name = "StrucDoc.Caption"

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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "linkHtml",
                    "type": ForwardRef("StrucDocLinkHtml"),
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
                    "name": "footnote",
                    "type": ForwardRef("StrucDocFootnote"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "footnoteRef",
                    "type": StrucDocFootnoteRef,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocRenderMultiMedia:
    class Meta:
        name = "StrucDoc.RenderMultiMedia"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    referenced_object: list[str] = field(
        default_factory=list,
        metadata={
            "name": "referencedObject",
            "type": "Attribute",
            "tokens": True,
        },
    )
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


@dataclass
class StrucDocContent:
    class Meta:
        name = "StrucDoc.Content"

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
    revised: Optional[StrucDocContentRevised] = field(
        default=None,
        metadata={
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
                    "type": ForwardRef("StrucDocContent"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "linkHtml",
                    "type": ForwardRef("StrucDocLinkHtml"),
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
                    "type": ForwardRef("StrucDocFootnote"),
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
            ),
        },
    )


@dataclass
class StrucDocFootnote:
    class Meta:
        name = "StrucDoc.Footnote"

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
                    "type": ForwardRef("StrucDocLinkHtml"),
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
                    "name": "renderMultiMedia",
                    "type": StrucDocRenderMultiMedia,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "paragraph",
                    "type": ForwardRef("StrucDocParagraph"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "list",
                    "type": ForwardRef("StrucDocList"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "table",
                    "type": ForwardRef("StrucDocTable"),
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocLinkHtml:
    class Meta:
        name = "StrucDoc.LinkHtml"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rev: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
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
            ),
        },
    )


@dataclass
class StrucDocParagraph:
    class Meta:
        name = "StrucDoc.Paragraph"

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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "caption",
                    "type": StrucDocCaption,
                    "namespace": "urn:hl7-org:v3",
                },
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
            ),
        },
    )


@dataclass
class StrucDocTh:
    class Meta:
        name = "StrucDoc.Th"

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
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headers: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: Optional[StrucDocThScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[StrucDocThAlign] = field(
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
    valign: Optional[StrucDocThValign] = field(
        default=None,
        metadata={
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
            ),
        },
    )


@dataclass
class StrucDocItem:
    class Meta:
        name = "StrucDoc.Item"

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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "caption",
                    "type": StrucDocCaption,
                    "namespace": "urn:hl7-org:v3",
                },
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
                    "type": ForwardRef("StrucDocList"),
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "table",
                    "type": ForwardRef("StrucDocTable"),
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )


@dataclass
class StrucDocList:
    class Meta:
        name = "StrucDoc.List"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    item: list[StrucDocItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
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
    list_type: StrucDocListListType = field(
        default=StrucDocListListType.UNORDERED,
        metadata={
            "name": "listType",
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTd:
    class Meta:
        name = "StrucDoc.Td"

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
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headers: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: Optional[StrucDocTdScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[StrucDocTdAlign] = field(
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
    valign: Optional[StrucDocTdValign] = field(
        default=None,
        metadata={
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
            ),
        },
    )


@dataclass
class StrucDocTr:
    class Meta:
        name = "StrucDoc.Tr"

    th: list[StrucDocTh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    td: list[StrucDocTd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
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
    align: Optional[StrucDocTrAlign] = field(
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
    valign: Optional[StrucDocTrValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTbody:
    class Meta:
        name = "StrucDoc.Tbody"

    tr: list[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
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
    align: Optional[StrucDocTbodyAlign] = field(
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
    valign: Optional[StrucDocTbodyValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTfoot:
    class Meta:
        name = "StrucDoc.Tfoot"

    tr: list[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
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
    align: Optional[StrucDocTfootAlign] = field(
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
    valign: Optional[StrucDocTfootValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocThead:
    class Meta:
        name = "StrucDoc.Thead"

    tr: list[StrucDocTr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
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
    align: Optional[StrucDocTheadAlign] = field(
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
    valign: Optional[StrucDocTheadValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrucDocTable:
    class Meta:
        name = "StrucDoc.Table"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    col: list[StrucDocCol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    colgroup: list[StrucDocColgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    thead: Optional[StrucDocThead] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    tfoot: Optional[StrucDocTfoot] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    tbody: list[StrucDocTbody] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
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
    summary: Optional[str] = field(
        default=None,
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
    border: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    frame: Optional[StrucDocTableFrame] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rules: Optional[StrucDocTableRules] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
