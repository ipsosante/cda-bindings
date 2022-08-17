from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.bl import Bl
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.external_act import ExternalAct
from cda.org.hl7.v3.external_document import ExternalDocument
from cda.org.hl7.v3.external_observation import ExternalObservation
from cda.org.hl7.v3.external_procedure import ExternalProcedure
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.x_act_relationship_external_reference import XActRelationshipExternalReference

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Reference:
    class Meta:
        name = "POCD_MT000040.Reference"

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
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    external_act: Optional[ExternalAct] = field(
        default=None,
        metadata={
            "name": "externalAct",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    external_observation: Optional[ExternalObservation] = field(
        default=None,
        metadata={
            "name": "externalObservation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    external_procedure: Optional[ExternalProcedure] = field(
        default=None,
        metadata={
            "name": "externalProcedure",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    external_document: Optional[ExternalDocument] = field(
        default=None,
        metadata={
            "name": "externalDocument",
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
    type_code: Optional[XActRelationshipExternalReference] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
