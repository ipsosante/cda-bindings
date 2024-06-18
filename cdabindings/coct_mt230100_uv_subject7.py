from dataclasses import dataclass, field
from typing import Optional

from cdabindings.all_infrastructure_root_template_id import (
    AllInfrastructureRootTemplateId,
)
from cdabindings.all_infrastructure_root_type_id import (
    AllInfrastructureRootTypeId,
)
from cdabindings.coct_mt440001_uv_valued_item import CoctMt440001UvValuedItem
from cdabindings.cs import CS

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class CoctMt230100UvSubject7:
    class Meta:
        name = "COCT_MT230100UV.Subject7"

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
    valued_item: Optional[CoctMt440001UvValuedItem] = field(
        default=None,
        metadata={
            "name": "valuedItem",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    null_flavor: Optional[str] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: str = field(
        init=False,
        default="SBJ",
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
