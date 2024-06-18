from dataclasses import dataclass, field
from typing import Optional

from cdabindings.act_relationship_type import ActRelationshipType
from cdabindings.criterion import Criterion
from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Precondition11:
    class Meta:
        name = "Precondition1"

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
    conjunction_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
            "required": True,
        },
    )
    criterion1: Optional[Criterion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
            "required": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ActRelationshipType = field(
        init=False,
        default=ActRelationshipType.PRCN,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
