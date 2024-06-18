from dataclasses import dataclass, field
from typing import Optional

from cdabindings.all_infrastructure_root_template_id import (
    AllInfrastructureRootTemplateId,
)
from cdabindings.all_infrastructure_root_type_id import (
    AllInfrastructureRootTypeId,
)
from cdabindings.cs import CS

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class CoctMt440001UvValuedItem:
    class Meta:
        name = "COCT_MT440001UV.ValuedItem"

    realm_code: list[CS] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[AllInfrastructureRootTypeId] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[AllInfrastructureRootTemplateId] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "min_occurs": 1,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    effective_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    unit_quantity: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitQuantity",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    unit_price_amt: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitPriceAmt",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "required": True,
        },
    )
    net_amt: Optional[str] = field(
        default=None,
        metadata={
            "name": "netAmt",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    class_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )
