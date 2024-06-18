from dataclasses import dataclass, field
from typing import Optional

from cdabindings.all_infrastructure_root_template_id import (
    AllInfrastructureRootTemplateId,
)
from cdabindings.all_infrastructure_root_type_id import (
    AllInfrastructureRootTypeId,
)
from cdabindings.coct_mt230100_uv_manufactured_product import (
    CoctMt230100UvManufacturedProduct,
)
from cdabindings.cs import CS

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class CoctMt230100UvPackagedMedicine:
    class Meta:
        name = "COCT_MT230100UV.PackagedMedicine"

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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    name: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    form_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "formCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    lot_number_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "lotNumberText",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    capacity_quantity: Optional[str] = field(
        default=None,
        metadata={
            "name": "capacityQuantity",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    cap_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "capTypeCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    as_manufactured_product: list[CoctMt230100UvManufacturedProduct] = field(
        default_factory=list,
        metadata={
            "name": "asManufacturedProduct",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    as_super_content: Optional["CoctMt230100UvSuperContent"] = field(
        default=None,
        metadata={
            "name": "asSuperContent",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    sub_content: Optional["CoctMt230100UvSubContent"] = field(
        default=None,
        metadata={
            "name": "subContent",
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
    class_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    determiner_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt230100UvSubContent:
    class Meta:
        name = "COCT_MT230100UV.SubContent"

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
    quantity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    contained_packaged_medicine: Optional[CoctMt230100UvPackagedMedicine] = (
        field(
            default=None,
            metadata={
                "name": "containedPackagedMedicine",
                "type": "Element",
                "namespace": "urn:ihe:pharm:medication",
                "nillable": True,
            },
        )
    )
    null_flavor: Optional[str] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
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


@dataclass
class CoctMt230100UvSuperContent:
    class Meta:
        name = "COCT_MT230100UV.SuperContent"

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
    quantity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    container_packaged_medicine: Optional[CoctMt230100UvPackagedMedicine] = (
        field(
            default=None,
            metadata={
                "name": "containerPackagedMedicine",
                "type": "Element",
                "namespace": "urn:ihe:pharm:medication",
                "required": True,
            },
        )
    )
    null_flavor: Optional[str] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
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
