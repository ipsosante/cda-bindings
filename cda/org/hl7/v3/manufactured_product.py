from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.labeled_drug import LabeledDrug
from cda.org.hl7.v3.material import Material
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.organization_part_of import Organization
from cda.org.hl7.v3.role_class_manufactured_product import RoleClassManufacturedProduct

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ManufacturedProduct:
    class Meta:
        name = "POCD_MT000040.ManufacturedProduct"

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
    manufactured_labeled_drug: Optional[LabeledDrug] = field(
        default=None,
        metadata={
            "name": "manufacturedLabeledDrug",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufactured_material: Optional[Material] = field(
        default=None,
        metadata={
            "name": "manufacturedMaterial",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufacturer_organization: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "manufacturerOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject_of1: List[str] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf1",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    subject_of2: List[str] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf2",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    subject_of3: List[str] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf3",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    subject_of4: List[str] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf4",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
        }
    )
    subject_of5: Optional[str] = field(
        default=None,
        metadata={
            "name": "subjectOf5",
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
    class_code: RoleClassManufacturedProduct = field(
        init=False,
        default=RoleClassManufacturedProduct.MANU,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
