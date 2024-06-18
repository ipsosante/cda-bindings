from dataclasses import dataclass, field
from typing import Optional

from cdabindings.assigned_entity import AssignedEntity
from cdabindings.ce import CE
from cdabindings.cs import CS
from cdabindings.function_code import FunctionCode
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.ivl_ts import IvlTs
from cdabindings.null_flavor import NullFlavor
from cdabindings.participation_physical_performer import (
    ParticipationPhysicalPerformer,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Performer2:
    class Meta:
        name = "POCD_MT000040.Performer2"

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
    function_code: Optional[FunctionCode] = field(
        default=None,
        metadata={
            "name": "functionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    mode_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_entity: Optional[AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
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
    type_code: ParticipationPhysicalPerformer = field(
        init=False,
        default=ParticipationPhysicalPerformer.PRF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
