from dataclasses import dataclass, field
from typing import Optional

from cdabindings.as_content import AsContent
from cdabindings.as_distributed_product import AsDistributedProduct
from cdabindings.as_medicine_manufacturer import AsMedicineManufacturer
from cdabindings.as_specialized_kind import AsSpecializedKind
from cdabindings.ce import CE
from cdabindings.cs import CS
from cdabindings.desc_2 import Desc2
from cdabindings.en import En
from cdabindings.entity_class_manufactured_material import (
    EntityClassManufacturedMaterial,
)
from cdabindings.entity_determiner_determined import EntityDeterminerDetermined
from cdabindings.expiration_time import ExpirationTime
from cdabindings.form_code import FormCode
from cdabindings.handling_code import HandlingCode
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.ingredient import Ingredient
from cdabindings.null_flavor import NullFlavor
from cdabindings.part import Part
from cdabindings.risk_code import RiskCode
from cdabindings.st import ST
from cdabindings.stability_time import StabilityTime

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Material:
    class Meta:
        name = "POCD_MT000040.Material"

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
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    name: Optional[En] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: Optional[Desc2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    risk_code: Optional[RiskCode] = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    handling_code: Optional[HandlingCode] = field(
        default=None,
        metadata={
            "name": "handlingCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    form_code: Optional[FormCode] = field(
        default=None,
        metadata={
            "name": "formCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    lot_number_text: Optional[ST] = field(
        default=None,
        metadata={
            "name": "lotNumberText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    expiration_time: Optional[ExpirationTime] = field(
        default=None,
        metadata={
            "name": "expirationTime",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    stability_time: Optional[StabilityTime] = field(
        default=None,
        metadata={
            "name": "stabilityTime",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        },
    )
    as_distributed_product: list[AsDistributedProduct] = field(
        default_factory=list,
        metadata={
            "name": "asDistributedProduct",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    as_medicine_manufacturer: list[AsMedicineManufacturer] = field(
        default_factory=list,
        metadata={
            "name": "asMedicineManufacturer",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    as_content: Optional[AsContent] = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    as_specialized_kind: list[AsSpecializedKind] = field(
        default_factory=list,
        metadata={
            "name": "asSpecializedKind",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    part: list[Part] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    ingredient: list[Ingredient] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassManufacturedMaterial = field(
        init=False,
        default=EntityClassManufacturedMaterial.MMAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    determiner_code: EntityDeterminerDetermined = field(
        init=False,
        default=EntityDeterminerDetermined.KIND,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        },
    )
