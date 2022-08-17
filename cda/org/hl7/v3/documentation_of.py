from dataclasses import dataclass, field
from typing import List, Optional, Union
from cda.org.hl7.v3.act_relationship_conditional import ActRelationshipConditional
from cda.org.hl7.v3.act_relationship_cost_tracking import ActRelationshipCostTracking
from cda.org.hl7.v3.act_relationship_has_component import ActRelationshipHasComponent
from cda.org.hl7.v3.act_relationship_outcome import ActRelationshipOutcome
from cda.org.hl7.v3.act_relationship_pertains_value import ActRelationshipPertainsValue
from cda.org.hl7.v3.act_relationship_posting import ActRelationshipPosting
from cda.org.hl7.v3.act_relationship_sequel import ActRelationshipSequel
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.has_support import HasSupport
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.service_event import ServiceEvent
from cda.org.hl7.v3.temporally_pertains import TemporallyPertains
from cda.org.hl7.v3.x_act_relationship_document import XActRelationshipDocument
from cda.org.hl7.v3.x_act_relationship_entry import XActRelationshipEntry
from cda.org.hl7.v3.x_act_relationship_entry_relationship import XActRelationshipEntryRelationship
from cda.org.hl7.v3.x_act_relationship_external_reference import XActRelationshipExternalReference
from cda.org.hl7.v3.x_act_relationship_patient_transport import XActRelationshipPatientTransport
from cda.org.hl7.v3.x_act_relationship_pertinent_info import XActRelationshipPertinentInfo

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class DocumentationOf:
    class Meta:
        name = "POCD_MT000040.DocumentationOf"

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
    service_event: Optional[ServiceEvent] = field(
        default=None,
        metadata={
            "name": "serviceEvent",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, str, ActRelationshipCostTracking, ActRelationshipPosting, TemporallyPertains, HasSupport, ActRelationshipPertainsValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo] = field(
        init=False,
        default=ActRelationshipSequel.DOC,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
