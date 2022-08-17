from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.intended_recipient import IntendedRecipient
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.x_information_recipient import XInformationRecipient

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class InformationRecipient:
    class Meta:
        name = "POCD_MT000040.InformationRecipient"

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
    intended_recipient: Optional[IntendedRecipient] = field(
        default=None,
        metadata={
            "name": "intendedRecipient",
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
    type_code: XInformationRecipient = field(
        default=XInformationRecipient.PRCP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
