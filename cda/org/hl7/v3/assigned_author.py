from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.ad import Ad
from cda.org.hl7.v3.authoring_device import AuthoringDevice
from cda.org.hl7.v3.cr import CE
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.organization_part_of import Organization
from cda.org.hl7.v3.person import Person
from cda.org.hl7.v3.role_class_assigned_entity import RoleClassAssignedEntity
from cda.org.hl7.v3.tel import Tel

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AssignedAuthor:
    class Meta:
        name = "POCD_MT000040.AssignedAuthor"

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
            "min_occurs": 1,
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
    assigned_person: Optional[Person] = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_authoring_device: Optional[AuthoringDevice] = field(
        default=None,
        metadata={
            "name": "assignedAuthoringDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    represented_organization: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "representedOrganization",
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
    class_code: RoleClassAssignedEntity = field(
        init=False,
        default=RoleClassAssignedEntity.ASSIGNED,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
