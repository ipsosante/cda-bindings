from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.bl import Bl
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class LanguageCommunication:
    class Meta:
        name = "POCD_MT000040.LanguageCommunication"

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
    language_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    mode_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    proficiency_level_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "proficiencyLevelCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    preference_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "preferenceInd",
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
