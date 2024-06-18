from dataclasses import dataclass, field
from typing import Optional

from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.labeled_drug import LabeledDrug
from cdabindings.material import Material
from cdabindings.null_flavor import NullFlavor
from cdabindings.organization import Organization
from cdabindings.role_class_manufactured_product import (
    RoleClassManufacturedProduct,
)
from cdabindings.subject_of1 import SubjectOf1
from cdabindings.subject_of2 import SubjectOf2
from cdabindings.subject_of3 import SubjectOf3
from cdabindings.subject_of4 import SubjectOf4
from cdabindings.subject_of5 import SubjectOf5

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ManufacturedProduct:
    class Meta:
        name = "POCD_MT000040.ManufacturedProduct"

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
    id: list[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    manufactured_labeled_drug: Optional[LabeledDrug] = field(
        default=None,
        metadata={
            "name": "manufacturedLabeledDrug",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    manufactured_material: Optional[Material] = field(
        default=None,
        metadata={
            "name": "manufacturedMaterial",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    manufacturer_organization: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "manufacturerOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    subject_of1: list[SubjectOf1] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf1",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of2: list[SubjectOf2] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf2",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of3: list[SubjectOf3] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf3",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of4: list[SubjectOf4] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf4",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of5: Optional[SubjectOf5] = field(
        default=None,
        metadata={
            "name": "subjectOf5",
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
    class_code: RoleClassManufacturedProduct = field(
        init=False,
        default=RoleClassManufacturedProduct.MANU,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
