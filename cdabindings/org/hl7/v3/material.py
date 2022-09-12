from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.v3.cr import CE
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.en import En
from cdabindings.org.hl7.v3.entity_class_manufactured_material import EntityClassManufacturedMaterial
from cdabindings.org.hl7.v3.entity_determiner_determined import EntityDeterminerDetermined
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.st import ST

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Material:
    class Meta:
        name = "POCD_MT000040.Material"

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
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: Optional[En] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    risk_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    handling_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "handlingCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    form_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "formCode",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    lot_number_text: Optional[ST] = field(
        default=None,
        metadata={
            "name": "lotNumberText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    expiration_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "expirationTime",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    stability_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "stabilityTime",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    as_distributed_product: List[str] = field(
        default_factory=list,
        metadata={
            "name": "asDistributedProduct",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    as_medicine_manufacturer: List[str] = field(
        default_factory=list,
        metadata={
            "name": "asMedicineManufacturer",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    as_content: Optional[str] = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    as_specialized_kind: List[str] = field(
        default_factory=list,
        metadata={
            "name": "asSpecializedKind",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    part: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    ingredient: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: EntityClassManufacturedMaterial = field(
        init=False,
        default=EntityClassManufacturedMaterial.MMAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminerDetermined = field(
        init=False,
        default=EntityDeterminerDetermined.KIND,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )
