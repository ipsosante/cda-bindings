from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.parent_document import ParentDocument
from cdabindings.org.hl7.v3.x_act_relationship_document import XActRelationshipDocument

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class RelatedDocument:
    class Meta:
        name = "POCD_MT000040.RelatedDocument"

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
    parent_document: Optional[ParentDocument] = field(
        default=None,
        metadata={
            "name": "parentDocument",
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
    type_code: Optional[XActRelationshipDocument] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
