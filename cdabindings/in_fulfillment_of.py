from dataclasses import dataclass, field
from typing import Optional

from cdabindings.act_relationship_fulfills import ActRelationshipFulfills
from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.in_fulfillment_of_2 import InFulfillmentOf2
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.order_2 import Order2


@dataclass
class DicomInFulfillmentOf(InFulfillmentOf2):
    class Meta:
        name = "inFulfillmentOf"
        namespace = "urn:dicom-org:ps3-20"


@dataclass
class InFulfillmentOf:
    class Meta:
        name = "POCD_MT000040.InFulfillmentOf"
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
    order: Optional[Order2] = field(
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
    type_code: ActRelationshipFulfills = field(
        init=False,
        default=ActRelationshipFulfills.FLFS,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
