from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.sdtc.act_reference import ActReference
from cda.org.hl7.v3.act_relationship_fulfills import ActRelationshipFulfills
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class InFulfillmentOf11:
    class Meta:
        name = "InFulfillmentOf1"

    realm_code: List[CS] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    type_id: Optional[InfrastructureRootTypeId] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    template_id: List[II] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    act_reference: Optional[ActReference] = field(
        default=None,
        metadata={
            "name": "actReference",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
            "required": True,
        }
    )
    type_code: ActRelationshipFulfills = field(
        init=False,
        default=ActRelationshipFulfills.FLFS,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    inversion_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "inversionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
