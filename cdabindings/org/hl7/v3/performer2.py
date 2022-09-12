from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.sdtc.function_code import FunctionCode
from cdabindings.org.hl7.v3.assigned_entity import AssignedEntity
from cdabindings.org.hl7.v3.cr import CE
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.ivl_ts import IvlTs
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.participation_physical_performer import ParticipationPhysicalPerformer

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Performer2:
    class Meta:
        name = "POCD_MT000040.Performer2"

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
    function_code: Optional[FunctionCode] = field(
        default=None,
        metadata={
            "name": "functionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    mode_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "modeCode",
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
    type_code: ParticipationPhysicalPerformer = field(
        init=False,
        default=ParticipationPhysicalPerformer.PRF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
