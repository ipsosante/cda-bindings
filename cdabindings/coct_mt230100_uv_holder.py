from dataclasses import dataclass, field
from typing import Optional

from cdabindings.all_infrastructure_root_template_id import (
    AllInfrastructureRootTemplateId,
)
from cdabindings.all_infrastructure_root_type_id import (
    AllInfrastructureRootTypeId,
)
from cdabindings.coct_mt230100_uv_role import CoctMt230100UvRole
from cdabindings.cs import CS

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class CoctMt230100UvHolder:
    class Meta:
        name = "COCT_MT230100UV.Holder"

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
    role: Optional[CoctMt230100UvRole] = field(
        default=None,
        metadata={
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
    type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )
