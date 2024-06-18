from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ad import Ad
from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.organization import Organization
from cdabindings.person import Person
from cdabindings.tel import Tel
from cdabindings.x_information_recipient_role import XInformationRecipientRole

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IntendedRecipient:
    class Meta:
        name = "POCD_MT000040.IntendedRecipient"

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
    addr: list[Ad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    telecom: list[Tel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    information_recipient: Optional[Person] = field(
        default=None,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    received_organization: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "receivedOrganization",
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
    class_code: XInformationRecipientRole = field(
        default=XInformationRecipientRole.ASSIGNED,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
