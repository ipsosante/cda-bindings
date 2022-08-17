from dataclasses import dataclass, field
from typing import List, Optional
from cda.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.status_code import StatusCode
from cda.org.hl7.v3.act_class_root import ActClassRoot
from cda.org.hl7.v3.act_mood import ActMood
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.ivl_ts import IvlTs
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.performer1 import Performer1

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ServiceEvent:
    class Meta:
        name = "POCD_MT000040.ServiceEvent"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
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
    status_code: Optional[StatusCode] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:oid:1.3.6.1.4.1.19376.1.3.2",
        }
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[Performer1] = field(
        default_factory=list,
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
    class_code: ActClassRoot = field(
        default=ActClassRoot.ACT,
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
