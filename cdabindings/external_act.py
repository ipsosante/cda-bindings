from dataclasses import dataclass, field
from typing import Optional

from cdabindings.act_class_root import ActClassRoot
from cdabindings.act_mood import ActMood
from cdabindings.cd import CD
from cdabindings.cs import CS
from cdabindings.ed import ED
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ExternalAct:
    class Meta:
        name = "POCD_MT000040.ExternalAct"

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
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClassRoot = field(
        default=ActClassRoot.ACT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        },
    )