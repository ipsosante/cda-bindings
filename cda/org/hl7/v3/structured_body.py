from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.act_class import ActClass
from cda.org.hl7.v3.act_mood import ActMood
from cda.org.hl7.v3.component3 import Component3
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StructuredBody:
    class Meta:
        name = "POCD_MT000040.StructuredBody"

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
    confidentiality_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component: List[Component3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.DOCBODY,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        }
    )
