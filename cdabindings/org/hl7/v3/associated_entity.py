from dataclasses import dataclass, field
from typing import List, Optional, Union
from cdabindings.org.hl7.v3.ad import Ad
from cdabindings.org.hl7.v3.cr import CE
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.organization_part_of import Organization
from cdabindings.org.hl7.v3.person import Person
from cdabindings.org.hl7.v3.role_class_mutual_relationship import RoleClassMutualRelationship
from cdabindings.org.hl7.v3.role_class_passive import RoleClassPassive
from cdabindings.org.hl7.v3.tel import Tel

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AssociatedEntity:
    class Meta:
        name = "POCD_MT000040.AssociatedEntity"

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
    addr: List[Ad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    telecom: List[Tel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    associated_person: Optional[Person] = field(
        default=None,
        metadata={
            "name": "associatedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    scoping_organization: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "scopingOrganization",
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
    class_code: Optional[Union[str, RoleClassMutualRelationship, RoleClassPassive]] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
