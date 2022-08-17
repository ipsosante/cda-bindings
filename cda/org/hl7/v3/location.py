from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.health_care_facility import HealthCareFacility
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.participation_target_location import ParticipationTargetLocation

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Location:
    class Meta:
        name = "POCD_MT000040.Location"

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
    health_care_facility: Optional[HealthCareFacility] = field(
        default=None,
        metadata={
            "name": "healthCareFacility",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationTargetLocation = field(
        init=False,
        default=ParticipationTargetLocation.LOC,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
