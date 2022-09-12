from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.sdtc.as_patient_relationship import AsPatientRelationship
from cdabindings.org.hl7.sdtc.desc import Desc
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.entity_class import EntityClass
from cdabindings.org.hl7.v3.entity_determiner import EntityDeterminer
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.pn import PN

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Person:
    class Meta:
        name = "POCD_MT000040.Person"

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
    name: List[PN] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    desc: Optional[Desc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    as_patient_relationship: Optional[AsPatientRelationship] = field(
        default=None,
        metadata={
            "name": "asPatientRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.PSN,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )
