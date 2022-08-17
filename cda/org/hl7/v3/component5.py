from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.act_class import ActClass
from cda.org.hl7.v3.act_mood import ActMood
from cda.org.hl7.v3.act_relationship_has_component import ActRelationshipHasComponent
from cda.org.hl7.v3.author import Author
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.entry import Entry
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.informant12 import Informant12
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.st import ST
from cda.org.hl7.v3.struc_doc_text import StrucDocText
from cda.org.hl7.v3.subject import Subject

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Component5:
    class Meta:
        name = "POCD_MT000040.Component5"

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
    section: Optional["Section"] = field(
        default=None,
        metadata={
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
    type_code: ActRelationshipHasComponent = field(
        init=False,
        default=ActRelationshipHasComponent.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        init=False,
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class Section:
    class Meta:
        name = "POCD_MT000040.Section"

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
    id: Optional[II] = field(
        default=None,
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
    title: Optional[ST] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[StrucDocText] = field(
        default=None,
        metadata={
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
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry: List[Entry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component: List[Component5] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
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
        default=ActClass.DOCSECT,
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
