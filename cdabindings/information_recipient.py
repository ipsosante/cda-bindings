from dataclasses import dataclass, field
from typing import Optional

from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.intended_recipient import IntendedRecipient
from cdabindings.null_flavor import NullFlavor
from cdabindings.x_information_recipient import XInformationRecipient

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class InformationRecipient:
    class Meta:
        name = "POCD_MT000040.InformationRecipient"

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
    intended_recipient: Optional[IntendedRecipient] = field(
        default=None,
        metadata={
            "name": "intendedRecipient",
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
    type_code: XInformationRecipient = field(
        default=XInformationRecipient.PRCP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
