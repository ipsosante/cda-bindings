from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ce import CE
from cdabindings.context_control import ContextControl
from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.ivl_ts import IvlTs
from cdabindings.null_flavor import NullFlavor
from cdabindings.participant_role import ParticipantRole
from cdabindings.participation_type import ParticipationType

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Participant2:
    class Meta:
        name = "POCD_MT000040.Participant2"

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
    time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    awareness_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "awarenessCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    participant_role: Optional[ParticipantRole] = field(
        default=None,
        metadata={
            "name": "participantRole",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: Optional[ParticipationType] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )
