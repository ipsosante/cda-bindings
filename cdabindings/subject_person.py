from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ce import CE
from cdabindings.cs import CS
from cdabindings.deceased_ind import DeceasedInd
from cdabindings.deceased_time import DeceasedTime
from cdabindings.desc_1 import Desc1
from cdabindings.entity_class import EntityClass
from cdabindings.entity_determiner import EntityDeterminer
from cdabindings.ethnic_group_code import EthnicGroupCode
from cdabindings.id_1 import Id1
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.multiple_birth_ind import MultipleBirthInd
from cdabindings.multiple_birth_order_number import MultipleBirthOrderNumber
from cdabindings.null_flavor import NullFlavor
from cdabindings.pn import PN
from cdabindings.race_code import RaceCode
from cdabindings.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class SubjectPerson:
    class Meta:
        name = "POCD_MT000040.SubjectPerson"

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
    id: list[Id1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
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
    administrative_gender_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "administrativeGenderCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    birth_time: Optional[TS] = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    deceased_ind: Optional[DeceasedInd] = field(
        default=None,
        metadata={
            "name": "deceasedInd",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    deceased_time: Optional[DeceasedTime] = field(
        default=None,
        metadata={
            "name": "deceasedTime",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    multiple_birth_ind: Optional[MultipleBirthInd] = field(
        default=None,
        metadata={
            "name": "multipleBirthInd",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    multiple_birth_order_number: Optional[MultipleBirthOrderNumber] = field(
        default=None,
        metadata={
            "name": "multipleBirthOrderNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    race_code: list[RaceCode] = field(
        default_factory=list,
        metadata={
            "name": "raceCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    ethnic_group_code: list[EthnicGroupCode] = field(
        default_factory=list,
        metadata={
            "name": "ethnicGroupCode",
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
