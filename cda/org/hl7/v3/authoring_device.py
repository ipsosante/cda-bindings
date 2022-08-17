from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.entity_class_device import EntityClassDevice
from cda.org.hl7.v3.entity_determiner import EntityDeterminer
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.maintained_entity import MaintainedEntity
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.sc import Sc

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AuthoringDevice:
    class Meta:
        name = "POCD_MT000040.AuthoringDevice"

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
    manufacturer_model_name: Optional[Sc] = field(
        default=None,
        metadata={
            "name": "manufacturerModelName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    software_name: Optional[Sc] = field(
        default=None,
        metadata={
            "name": "softwareName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    as_maintained_entity: List[MaintainedEntity] = field(
        default_factory=list,
        metadata={
            "name": "asMaintainedEntity",
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
    class_code: EntityClassDevice = field(
        init=False,
        default=EntityClassDevice.DEV,
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
