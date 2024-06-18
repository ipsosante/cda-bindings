from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ad import Ad
from cdabindings.ce import CE
from cdabindings.cs import CS
from cdabindings.id_1 import Id1
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.subject_person import SubjectPerson
from cdabindings.tel import Tel
from cdabindings.x_document_subject import XDocumentSubject

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class RelatedSubject:
    class Meta:
        name = "POCD_MT000040.RelatedSubject"

    realm_code: list[CS] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[InfrastructureRootTypeId] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[II] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Id1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    addr: list[Ad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    telecom: list[Tel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    subject: Optional[SubjectPerson] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: XDocumentSubject = field(
        default=XDocumentSubject.PRS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
