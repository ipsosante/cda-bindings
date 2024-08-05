from dataclasses import dataclass, field
from typing import Optional

from cdabindings.act_class_observation import ActClassObservation
from cdabindings.act_mood import ActMood
from cdabindings.any_abstract import AnyAbstract
from cdabindings.cd import CD
from cdabindings.code import Code
from cdabindings.criterion_class_code import CriterionClassCode
from cdabindings.criterion_mood_code import CriterionMoodCode
from cdabindings.cs import CS
from cdabindings.ed import ED
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.value import Value


@dataclass
class Criterion:
    class Meta:
        name = "POCD_MT000040.Criterion"
        target_namespace = "urn:hl7-org:v3"

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


@dataclass
class LabCriterion:
    class Meta:
        target_namespace = "urn:oid:1.3.6.1.4.1.19376.1.3.2"

    code: Optional[Code] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oid:1.3.6.1.4.1.19376.1.3.2",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oid:1.3.6.1.4.1.19376.1.3.2",
        },
    )
    class_code: Optional[CriterionClassCode] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    mood_code: Optional[CriterionMoodCode] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        },
    )
