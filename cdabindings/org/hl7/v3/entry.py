from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.encounter import (
    Act,
    Encounter,
    Observation,
    ObservationMedia,
    Organizer,
    Procedure,
    RegionOfInterest,
    SubstanceAdministration,
    Supply,
)
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.x_act_relationship_entry import XActRelationshipEntry

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Entry:
    class Meta:
        name = "POCD_MT000040.Entry"

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
    act: Optional[Act] = field(
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
    type_code: XActRelationshipEntry = field(
        default=XActRelationshipEntry.COMP,
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
