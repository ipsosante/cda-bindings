from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.v3.act_relationship_has_component import ActRelationshipHasComponent
from cdabindings.org.hl7.v3.component5 import Section
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Component3:
    class Meta:
        name = "POCD_MT000040.Component3"

    realm_code: List[CS] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[InfrastructureRootTypeId] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[II] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    section: Optional[Section] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ActRelationshipHasComponent = field(
        init=False,
        default=ActRelationshipHasComponent.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        init=False,
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
