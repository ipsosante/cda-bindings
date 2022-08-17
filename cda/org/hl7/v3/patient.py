from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.sdtc.deceased_ind import DeceasedInd
from cda.org.hl7.sdtc.deceased_time import DeceasedTime
from cda.org.hl7.sdtc.desc import Desc
from cda.org.hl7.sdtc.ethnic_group_code import EthnicGroupCode
from cda.org.hl7.sdtc.multiple_birth_ind import MultipleBirthInd
from cda.org.hl7.sdtc.multiple_birth_order_number import MultipleBirthOrderNumber
from cda.org.hl7.sdtc.race_code import RaceCode
from cda.org.hl7.v3.birthplace import Birthplace
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.entity_class import EntityClass
from cda.org.hl7.v3.entity_determiner import EntityDeterminer
from cda.org.hl7.v3.guardian import Guardian
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.language_communication import LanguageCommunication
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.pn import PN
from cda.org.hl7.v3.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Patient:
    class Meta:
        name = "POCD_MT000040.Patient"

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
    id: Optional[II] = field(
        default=None,
        metadata={
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
    administrative_gender_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "administrativeGenderCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    birth_time: Optional[TS] = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    deceased_ind: Optional[DeceasedInd] = field(
        default=None,
        metadata={
            "name": "deceasedInd",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    deceased_time: Optional[DeceasedTime] = field(
        default=None,
        metadata={
            "name": "deceasedTime",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    multiple_birth_ind: Optional[MultipleBirthInd] = field(
        default=None,
        metadata={
            "name": "multipleBirthInd",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    multiple_birth_order_number: Optional[MultipleBirthOrderNumber] = field(
        default=None,
        metadata={
            "name": "multipleBirthOrderNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    marital_status_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "maritalStatusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    religious_affiliation_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "religiousAffiliationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    race_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "raceCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    hl7_org_sdtc_race_code: List[RaceCode] = field(
        default_factory=list,
        metadata={
            "name": "raceCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    ethnic_group_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "ethnicGroupCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    hl7_org_sdtc_ethnic_group_code: List[EthnicGroupCode] = field(
        default_factory=list,
        metadata={
            "name": "ethnicGroupCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    guardian: List[Guardian] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    birthplace: Optional[Birthplace] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_communication: List[LanguageCommunication] = field(
        default_factory=list,
        metadata={
            "name": "languageCommunication",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
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
