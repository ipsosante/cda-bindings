from dataclasses import dataclass, field
from typing import Optional

from cdabindings.bl import BL
from cdabindings.cs import CS
from cdabindings.external_act import ExternalAct
from cdabindings.external_document import ExternalDocument
from cdabindings.external_observation import ExternalObservation
from cdabindings.external_procedure import ExternalProcedure
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.x_act_relationship_external_reference import (
    XActRelationshipExternalReference,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Reference:
    class Meta:
        name = "POCD_MT000040.Reference"

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
    seperatable_ind: Optional[BL] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    external_act: Optional[ExternalAct] = field(
        default=None,
        metadata={
            "name": "externalAct",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    external_observation: Optional[ExternalObservation] = field(
        default=None,
        metadata={
            "name": "externalObservation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    external_procedure: Optional[ExternalProcedure] = field(
        default=None,
        metadata={
            "name": "externalProcedure",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    external_document: Optional[ExternalDocument] = field(
        default=None,
        metadata={
            "name": "externalDocument",
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
    type_code: Optional[XActRelationshipExternalReference] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )
