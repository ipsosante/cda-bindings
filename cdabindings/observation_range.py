from dataclasses import dataclass, field
from typing import Optional

from cdabindings.act_class_observation import ActClassObservation
from cdabindings.act_mood import ActMood
from cdabindings.any_abstract import AnyAbstract
from cdabindings.cd import CD
from cdabindings.ce import CE
from cdabindings.cs import CS
from cdabindings.ed import ED
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.precondition import Precondition
from cdabindings.precondition1 import Precondition1

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ObservationRange:
    class Meta:
        name = "POCD_MT000040.ObservationRange"

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
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    text: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    value: Optional[AnyAbstract] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    interpretation_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "interpretationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    precondition1: list[Precondition1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    precondition: list[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oid:1.3.6.1.4.1.19376.1.3.2",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClassObservation = field(
        default=ActClassObservation.OBS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN_CRT,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        },
    )
