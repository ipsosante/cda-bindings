from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ce import CE
from cdabindings.cs import CS
from cdabindings.entity_determiner import EntityDeterminer
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.x_document_subject import XDocumentSubject

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class AsPatientRelationship1:
    class Meta:
        name = "AsPatientRelationship"

    realm_code: list[CS] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    type_id: Optional[InfrastructureRootTypeId] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    template_id: list[II] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
            "required": True,
        },
    )
    class_code: XDocumentSubject = field(
        init=False,
        default=XDocumentSubject.PRS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        },
    )
