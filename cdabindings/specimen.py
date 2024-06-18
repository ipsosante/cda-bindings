from dataclasses import dataclass, field
from typing import Optional

from cdabindings.cs import CS
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.null_flavor import NullFlavor
from cdabindings.participation_type import ParticipationType
from cdabindings.specimen_role import SpecimenRole

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Specimen:
    class Meta:
        name = "POCD_MT000040.Specimen"

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
    specimen_role: Optional[SpecimenRole] = field(
        default=None,
        metadata={
            "name": "specimenRole",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.SPC,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
