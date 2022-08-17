from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.assigned_entity import AssignedEntity
from cda.org.hl7.v3.context_control import ContextControl
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.participation_type import ParticipationType
from cda.org.hl7.v3.related_entity import RelatedEntity

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Informant12:
    class Meta:
        name = "POCD_MT000040.Informant12"

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
    assigned_entity: Optional[AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_entity: Optional[RelatedEntity] = field(
        default=None,
        metadata={
            "name": "relatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.INF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
