from dataclasses import dataclass, field
from typing import Optional

from cdabindings.all_infrastructure_root_template_id import (
    AllInfrastructureRootTemplateId,
)
from cdabindings.all_infrastructure_root_type_id import (
    AllInfrastructureRootTypeId,
)
from cdabindings.coct_mt230100_uv_manufacturer import (
    CoctMt230100UvManufacturer,
)
from cdabindings.coct_mt230100_uv_subject15 import CoctMt230100UvSubject15
from cdabindings.coct_mt230100_uv_subject16 import CoctMt230100UvSubject16
from cdabindings.coct_mt230100_uv_subject25 import CoctMt230100UvSubject25
from cdabindings.cs import CS

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class CoctMt230100UvManufacturedProduct:
    class Meta:
        name = "COCT_MT230100UV.ManufacturedProduct"

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
    manufacturer: Optional[CoctMt230100UvManufacturer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "required": True,
        },
    )
    subject_of1: list[CoctMt230100UvSubject25] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf1",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of2: list[CoctMt230100UvSubject15] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf2",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of3: list[CoctMt230100UvSubject16] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf3",
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
