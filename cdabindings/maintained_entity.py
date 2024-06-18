from dataclasses import dataclass, field
from typing import Optional

from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.ivl_ts import IvlTs
from cdabindings.null_flavor import NullFlavor
from cdabindings.person import Person
from cdabindings.role_class import RoleClass

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class MaintainedEntity:
    class Meta:
        name = "POCD_MT000040.MaintainedEntity"

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
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    maintaining_person: Optional[Person] = field(
        default=None,
        metadata={
            "name": "maintainingPerson",
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
    class_code: RoleClass = field(
        init=False,
        default=RoleClass.MNT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
