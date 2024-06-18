from dataclasses import dataclass, field
from typing import Optional

from cdabindings.act_relationship_has_component import (
    ActRelationshipHasComponent,
)
from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.non_xmlbody import NonXmlbody
from cdabindings.null_flavor import NullFlavor
from cdabindings.structured_body import StructuredBody

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Component2:
    class Meta:
        name = "POCD_MT000040.Component2"

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
    non_xmlbody: Optional[NonXmlbody] = field(
        default=None,
        metadata={
            "name": "nonXMLBody",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    structured_body: Optional[StructuredBody] = field(
        default=None,
        metadata={
            "name": "structuredBody",
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
    type_code: ActRelationshipHasComponent = field(
        init=False,
        default=ActRelationshipHasComponent.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
    context_conduction_ind: str = field(
        init=False,
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )
