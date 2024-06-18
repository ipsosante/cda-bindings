from dataclasses import dataclass, field
from typing import Optional

from cdabindings.act_relationship_type import ActRelationshipType
from cdabindings.criterion import (
    Criterion,
)
from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.precondition_type_code import PreconditionTypeCode


@dataclass
class Precondition:
    class Meta:
        name = "POCD_MT000040.Precondition"
        target_namespace = "urn:hl7-org:v3"

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
    criterion: Optional[Criterion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
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


@dataclass
class Precondition:
    class Meta:
        name = "precondition"
        namespace = "urn:oid:1.3.6.1.4.1.19376.1.3.2"

    criterion: Optional[Criterion] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_code: Optional[PreconditionTypeCode] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
