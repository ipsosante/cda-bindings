from dataclasses import dataclass, field
from typing import Optional

from cdabindings.cs import CS
from cdabindings.custodian_organization import CustodianOrganization
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.role_class_assigned_entity import RoleClassAssignedEntity

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AssignedCustodian:
    class Meta:
        name = "POCD_MT000040.AssignedCustodian"

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
    represented_custodian_organization: Optional[CustodianOrganization] = (
        field(
            default=None,
            metadata={
                "name": "representedCustodianOrganization",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "required": True,
            },
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassAssignedEntity = field(
        init=False,
        default=RoleClassAssignedEntity.ASSIGNED,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
