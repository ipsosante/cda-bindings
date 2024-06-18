from dataclasses import dataclass, field
from typing import Optional

from cdabindings.as_patient_relationship import AsPatientRelationship
from cdabindings.cs import CS
from cdabindings.desc_1 import Desc1
from cdabindings.entity_class import EntityClass
from cdabindings.entity_determiner import EntityDeterminer
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.pn import PN

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Person:
    class Meta:
        name = "POCD_MT000040.Person"

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
    name: list[PN] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: Optional[Desc1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    as_patient_relationship: Optional[AsPatientRelationship] = field(
        default=None,
        metadata={
            "name": "asPatientRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.PSN,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        },
    )
