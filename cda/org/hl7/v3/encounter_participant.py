from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.assigned_entity import AssignedEntity
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.ivl_ts import IvlTs
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.x_encounter_participant import XEncounterParticipant

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class EncounterParticipant:
    class Meta:
        name = "POCD_MT000040.EncounterParticipant"

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
    time: Optional[IvlTs] = field(
        default=None,
        metadata={
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
    type_code: Optional[XEncounterParticipant] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
