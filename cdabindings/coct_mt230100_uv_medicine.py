from dataclasses import dataclass, field
from typing import Optional

from cdabindings.all_infrastructure_root_template_id import (
    AllInfrastructureRootTemplateId,
)
from cdabindings.all_infrastructure_root_type_id import (
    AllInfrastructureRootTypeId,
)
from cdabindings.coct_mt230100_uv_content import CoctMt230100UvContent
from cdabindings.coct_mt230100_uv_distributed_product import (
    CoctMt230100UvDistributedProduct,
)
from cdabindings.coct_mt230100_uv_ingredient import CoctMt230100UvIngredient
from cdabindings.coct_mt230100_uv_medicine_manufacturer import (
    CoctMt230100UvMedicineManufacturer,
)
from cdabindings.coct_mt230100_uv_specialized_kind import (
    CoctMt230100UvSpecializedKind,
)
from cdabindings.coct_mt230100_uv_subject4 import CoctMt230100UvSubject4
from cdabindings.cs import CS

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class CoctMt230100UvMedicine:
    class Meta:
        name = "COCT_MT230100UV.Medicine"

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
    desc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    risk_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    handling_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "handlingCode",
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
    expiration_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "expirationTime",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    stability_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "stabilityTime",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    as_distributed_product: list[CoctMt230100UvDistributedProduct] = field(
        default_factory=list,
        metadata={
            "name": "asDistributedProduct",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    as_medicine_manufacturer: list[CoctMt230100UvMedicineManufacturer] = field(
        default_factory=list,
        metadata={
            "name": "asMedicineManufacturer",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    as_content: Optional[CoctMt230100UvContent] = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    as_specialized_kind: list[CoctMt230100UvSpecializedKind] = field(
        default_factory=list,
        metadata={
            "name": "asSpecializedKind",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    part: list["CoctMt230100UvPart"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    ingredient: list[CoctMt230100UvIngredient] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
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
class CoctMt230100UvPart:
    class Meta:
        name = "COCT_MT230100UV.Part"

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
    part_medicine: Optional[CoctMt230100UvMedicine] = field(
        default=None,
        metadata={
            "name": "partMedicine",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "required": True,
        },
    )
    subject_of: list[CoctMt230100UvSubject4] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf",
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
