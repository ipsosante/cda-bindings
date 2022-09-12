from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.sdtc.discharge_disposition_code import DischargeDispositionCode
from cdabindings.org.hl7.sdtc.in_fulfillment_of1 import InFulfillmentOf1
from cdabindings.org.hl7.sdtc.priority_number import PriorityNumber
from cdabindings.org.hl7.sdtc.text import Text
from cdabindings.org.hl7.v3.act_class import ActClass
from cdabindings.org.hl7.v3.act_class_observation import ActClassObservation
from cdabindings.org.hl7.v3.act_class_supply import ActClassSupply
from cdabindings.org.hl7.v3.act_mood import ActMood
from cdabindings.org.hl7.v3.act_relationship_has_component import ActRelationshipHasComponent
from cdabindings.org.hl7.v3.any import Any
from cdabindings.org.hl7.v3.author import Author
from cdabindings.org.hl7.v3.bl import Bl
from cdabindings.org.hl7.v3.consumable import Consumable
from cdabindings.org.hl7.v3.cr import (
    CD,
    CE,
)
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.ed import ED
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.informant12 import Informant12
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.int_mod import Int
from cdabindings.org.hl7.v3.ivl_int import IvlInt
from cdabindings.org.hl7.v3.ivl_pq import IvlPq
from cdabindings.org.hl7.v3.ivl_ts import IvlTs
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.participant2 import Participant2
from cdabindings.org.hl7.v3.performer2 import Performer2
from cdabindings.org.hl7.v3.pq import Pq
from cdabindings.org.hl7.v3.precondition import Precondition
from cdabindings.org.hl7.v3.product import Product
from cdabindings.org.hl7.v3.reference import Reference
from cdabindings.org.hl7.v3.reference_range import ReferenceRange
from cdabindings.org.hl7.v3.region_of_interest_value import RegionOfInterestValue
from cdabindings.org.hl7.v3.rto_pq_pq import RtoPqPq
from cdabindings.org.hl7.v3.specimen import Specimen
from cdabindings.org.hl7.v3.st import ST
from cdabindings.org.hl7.v3.subject import Subject
from cdabindings.org.hl7.v3.sxcm_ts import SxcmTs
from cdabindings.org.hl7.v3.x_act_class_document_entry_act import XActClassDocumentEntryAct
from cdabindings.org.hl7.v3.x_act_class_document_entry_organizer import XActClassDocumentEntryOrganizer
from cdabindings.org.hl7.v3.x_act_mood_document_observation import XActMoodDocumentObservation
from cdabindings.org.hl7.v3.x_act_relationship_entry_relationship import XActRelationshipEntryRelationship
from cdabindings.org.hl7.v3.x_document_act_mood import XDocumentActMood
from cdabindings.org.hl7.v3.x_document_encounter_mood import XDocumentEncounterMood
from cdabindings.org.hl7.v3.x_document_procedure_mood import XDocumentProcedureMood
from cdabindings.org.hl7.v3.x_document_substance_mood import XDocumentSubstanceMood

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Encounter:
    class Meta:
        name = "POCD_MT000040.Encounter"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    discharge_disposition_code: Optional[DischargeDispositionCode] = field(
        default=None,
        metadata={
            "name": "dischargeDispositionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    priority_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of1: List[InFulfillmentOf1] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClass] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentEncounterMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Observation:
    class Meta:
        name = "POCD_MT000040.Observation"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    derivation_expr: Optional[ST] = field(
        default=None,
        metadata={
            "name": "derivationExpr",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata={
            "name": "repeatNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: List[Any] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    interpretation_code: List[CE] = field(
        default_factory=list,
        metadata={
            "name": "interpretationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    method_code: List[CE] = field(
        default_factory=list,
        metadata={
            "name": "methodCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    target_site_code: List[CD] = field(
        default_factory=list,
        metadata={
            "name": "targetSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference_range: List[ReferenceRange] = field(
        default_factory=list,
        metadata={
            "name": "referenceRange",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of1: List[InFulfillmentOf1] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XActMoodDocumentObservation] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
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


@dataclass
class ObservationMedia:
    class Meta:
        name = "POCD_MT000040.ObservationMedia"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[ActMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Procedure:
    class Meta:
        name = "POCD_MT000040.Procedure"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    method_code: List[CE] = field(
        default_factory=list,
        metadata={
            "name": "methodCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    approach_site_code: List[CD] = field(
        default_factory=list,
        metadata={
            "name": "approachSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    target_site_code: List[CD] = field(
        default_factory=list,
        metadata={
            "name": "targetSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of1: List[InFulfillmentOf1] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClass] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentProcedureMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
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


@dataclass
class RegionOfInterest:
    class Meta:
        name = "POCD_MT000040.RegionOfInterest"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    code: Optional[CS] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    value: List[RegionOfInterestValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.ROIOVL,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SubstanceAdministration:
    class Meta:
        name = "POCD_MT000040.SubstanceAdministration"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: List[SxcmTs] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata={
            "name": "repeatNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    route_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "routeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    approach_site_code: List[CD] = field(
        default_factory=list,
        metadata={
            "name": "approachSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    dose_quantity: Optional[IvlPq] = field(
        default=None,
        metadata={
            "name": "doseQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    rate_quantity: Optional[IvlPq] = field(
        default=None,
        metadata={
            "name": "rateQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    max_dose_quantity: Optional[RtoPqPq] = field(
        default=None,
        metadata={
            "name": "maxDoseQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    administration_unit_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "administrationUnitCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    consumable: Optional[Consumable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of1: List[InFulfillmentOf1] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.SBADM,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentSubstanceMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
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


@dataclass
class Supply:
    class Meta:
        name = "POCD_MT000040.Supply"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: List[SxcmTs] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_code: List[CE] = field(
        default_factory=list,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata={
            "name": "repeatNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    independent_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "independentInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    quantity: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    expected_use_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "expectedUseTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    product: Optional[Product] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of1: List[InFulfillmentOf1] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClassSupply = field(
        init=False,
        default=ActClassSupply.SPLY,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentSubstanceMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Component4:
    class Meta:
        name = "POCD_MT000040.Component4"

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
    sequence_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_number: Optional[PriorityNumber] = field(
        default=None,
        metadata={
            "name": "priorityNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
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
    act: Optional["Act"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    encounter: Optional[Encounter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation: Optional[Observation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation_media: Optional[ObservationMedia] = field(
        default=None,
        metadata={
            "name": "observationMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    organizer: Optional["Organizer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    procedure: Optional[Procedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    region_of_interest: Optional[RegionOfInterest] = field(
        default=None,
        metadata={
            "name": "regionOfInterest",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    substance_administration: Optional[SubstanceAdministration] = field(
        default=None,
        metadata={
            "name": "substanceAdministration",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    supply: Optional[Supply] = field(
        default=None,
        metadata={
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


@dataclass
class Organizer:
    class Meta:
        name = "POCD_MT000040.Organizer"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[Text] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component: List[Component4] = field(
        default_factory=list,
        metadata={
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
    class_code: Optional[XActClassDocumentEntryOrganizer] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[ActMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class EntryRelationship:
    class Meta:
        name = "POCD_MT000040.EntryRelationship"

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
    sequence_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
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
    act: Optional["Act"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    encounter: Optional[Encounter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation: Optional[Observation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation_media: Optional[ObservationMedia] = field(
        default=None,
        metadata={
            "name": "observationMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    organizer: Optional[Organizer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    procedure: Optional[Procedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    region_of_interest: Optional[RegionOfInterest] = field(
        default=None,
        metadata={
            "name": "regionOfInterest",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    substance_administration: Optional[SubstanceAdministration] = field(
        default=None,
        metadata={
            "name": "substanceAdministration",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    supply: Optional[Supply] = field(
        default=None,
        metadata={
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
    type_code: Optional[XActRelationshipEntryRelationship] = field(
        default=None,
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
    context_conduction_ind: str = field(
        default="true",
        metadata={
            "name": "contextConductionInd",
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


@dataclass
class Act:
    class Meta:
        name = "POCD_MT000040.Act"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    text: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List[EntryRelationship] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of1: List[InFulfillmentOf1] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[XActClassDocumentEntryAct] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentActMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
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
