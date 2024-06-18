from dataclasses import dataclass, field
from typing import Optional

from cdabindings.all_infrastructure_root_template_id import (
    AllInfrastructureRootTemplateId,
)
from cdabindings.all_infrastructure_root_type_id import (
    AllInfrastructureRootTypeId,
)
from cdabindings.coct_mt230100_uv_medicine import CoctMt230100UvMedicine
from cdabindings.coct_mt230100_uv_subject1 import CoctMt230100UvSubject1
from cdabindings.coct_mt230100_uv_subject2 import CoctMt230100UvSubject2
from cdabindings.coct_mt230100_uv_subject3 import CoctMt230100UvSubject3
from cdabindings.coct_mt230100_uv_subject7 import CoctMt230100UvSubject7
from cdabindings.coct_mt230100_uv_subject22 import CoctMt230100UvSubject22
from cdabindings.cs import CS

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class CoctMt230100UvMedication:
    class Meta:
        name = "COCT_MT230100UV.Medication"

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
    administerable_medicine: Optional[CoctMt230100UvMedicine] = field(
        default=None,
        metadata={
            "name": "administerableMedicine",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "required": True,
        },
    )
    subject_of1: list[CoctMt230100UvSubject2] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf1",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of2: list[CoctMt230100UvSubject1] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf2",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of3: list[CoctMt230100UvSubject22] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf3",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of4: list[CoctMt230100UvSubject3] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf4",
            "type": "Element",
            "namespace": "urn:ihe:pharm:medication",
            "nillable": True,
        },
    )
    subject_of5: Optional[CoctMt230100UvSubject7] = field(
        default=None,
        metadata={
            "name": "subjectOf5",
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
