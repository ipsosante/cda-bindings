from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.precondition import Precondition
from cdabindings.org.hl7.sdtc.precondition1 import Precondition1
from cdabindings.org.hl7.v3.act_class_observation import ActClassObservation
from cdabindings.org.hl7.v3.act_mood import ActMood
from cdabindings.org.hl7.v3.any import Any
from cdabindings.org.hl7.v3.cr import (
    CD,
    CE,
)
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.ed import ED
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ObservationRange:
    class Meta:
        name = "POCD_MT000040.ObservationRange"

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
    code: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[ED] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[Any] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    interpretation_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "interpretationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition1: List[Precondition1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    precondition: List[Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oid:1.3.6.1.4.1.19376.1.3.2",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClassObservation = field(
        default=ActClassObservation.OBS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN_CRT,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        }
    )
