from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.context_control import ContextControl
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.ivl_ts import IvlTs
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.participant_role import ParticipantRole
from cda.org.hl7.v3.participation_type import ParticipationType

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Participant2:
    class Meta:
        name = "POCD_MT000040.Participant2"

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
    function_code: Optional[object] = field(
        default=None,
        metadata={
            "name": "functionCode",
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
    awareness_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "awarenessCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant_role: Optional[ParticipantRole] = field(
        default=None,
        metadata={
            "name": "participantRole",
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
    type_code: Optional[ParticipationType] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
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
