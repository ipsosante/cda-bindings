from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.en import En
from cda.org.hl7.v3.entity_class_manufactured_material import EntityClassManufacturedMaterial
from cda.org.hl7.v3.entity_determiner_determined import EntityDeterminerDetermined
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class LabeledDrug:
    class Meta:
        name = "POCD_MT000040.LabeledDrug"

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
    name: Optional[En] = field(
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
    class_code: EntityClassManufacturedMaterial = field(
        init=False,
        default=EntityClassManufacturedMaterial.MMAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminerDetermined = field(
        init=False,
        default=EntityDeterminerDetermined.KIND,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )
