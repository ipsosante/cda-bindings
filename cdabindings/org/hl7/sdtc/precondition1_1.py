from dataclasses import dataclass, field
from typing import List, Optional, Union
from cdabindings.org.hl7.v3.act_relationship_conditional import ActRelationshipConditional
from cdabindings.org.hl7.v3.act_relationship_cost_tracking import ActRelationshipCostTracking
from cdabindings.org.hl7.v3.act_relationship_has_component import ActRelationshipHasComponent
from cdabindings.org.hl7.v3.act_relationship_outcome import ActRelationshipOutcome
from cdabindings.org.hl7.v3.act_relationship_pertains_value import ActRelationshipPertainsValue
from cdabindings.org.hl7.v3.act_relationship_posting import ActRelationshipPosting
from cdabindings.org.hl7.v3.act_relationship_sequel import ActRelationshipSequel
from cdabindings.org.hl7.v3.criterion import Criterion
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.has_support import HasSupport
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.temporally_pertains import TemporallyPertains
from cdabindings.org.hl7.v3.x_act_relationship_document import XActRelationshipDocument
from cdabindings.org.hl7.v3.x_act_relationship_entry import XActRelationshipEntry
from cdabindings.org.hl7.v3.x_act_relationship_entry_relationship import XActRelationshipEntryRelationship
from cdabindings.org.hl7.v3.x_act_relationship_external_reference import XActRelationshipExternalReference
from cdabindings.org.hl7.v3.x_act_relationship_patient_transport import XActRelationshipPatientTransport
from cdabindings.org.hl7.v3.x_act_relationship_pertinent_info import XActRelationshipPertinentInfo

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Precondition11:
    class Meta:
        name = "Precondition1"

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
    conjunction_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
            "required": True,
        }
    )
    criterion1: Optional[Criterion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
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
        default=ActRelationshipConditional.PRCN,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
