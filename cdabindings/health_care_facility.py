from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ce import CE
from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.organization import Organization
from cdabindings.place import Place
from cdabindings.role_class_service_delivery_location import (
    RoleClassServiceDeliveryLocation,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class HealthCareFacility:
    class Meta:
        name = "POCD_MT000040.HealthCareFacility"

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
    id: list[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    location: Optional[Place] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    service_provider_organization: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "serviceProviderOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassServiceDeliveryLocation = field(
        default=RoleClassServiceDeliveryLocation.SDLOC,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
