from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.sdtc.birth_time import BirthTime
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ed import ED
from cda.org.hl7.v3.entity_class_root import EntityClassRoot
from cda.org.hl7.v3.entity_determiner import EntityDeterminer
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.pn import PN
from cda.org.hl7.v3.pq import Pq

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PlayingEntity:
    class Meta:
        name = "POCD_MT000040.PlayingEntity"

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
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    quantity: List[Pq] = field(
        default_factory=list,
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
    birth_time: Optional[BirthTime] = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    desc: Optional[ED] = field(
        default=None,
        metadata={
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
    class_code: EntityClassRoot = field(
        default=EntityClassRoot.ENT,
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
