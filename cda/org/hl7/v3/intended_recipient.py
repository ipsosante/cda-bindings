from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.ad import Ad
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.organization_part_of import Organization
from cda.org.hl7.v3.person import Person
from cda.org.hl7.v3.tel import Tel
from cda.org.hl7.v3.x_information_recipient_role import XInformationRecipientRole

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IntendedRecipient:
    class Meta:
        name = "POCD_MT000040.IntendedRecipient"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    addr: List[Ad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    telecom: List[Tel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    information_recipient: Optional[Person] = field(
        default=None,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    received_organization: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "receivedOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: XInformationRecipientRole = field(
        default=XInformationRecipientRole.ASSIGNED,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
