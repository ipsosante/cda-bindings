from dataclasses import dataclass, field
from typing import List, Optional, Union
from cdabindings.org.hl7.v3.ad import Ad
from cdabindings.org.hl7.v3.cr import CE
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.device import Device
from cdabindings.org.hl7.v3.entity import Entity
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.playing_entity import PlayingEntity
from cdabindings.org.hl7.v3.role_class_mutual_relationship import RoleClassMutualRelationship
from cdabindings.org.hl7.v3.role_class_ontological import RoleClassOntological
from cdabindings.org.hl7.v3.role_class_partitive import RoleClassPartitive
from cdabindings.org.hl7.v3.role_class_passive import RoleClassPassive
from cdabindings.org.hl7.v3.role_class_root_value import RoleClassRootValue
from cdabindings.org.hl7.v3.tel import Tel
from cdabindings.org.hl7.v3.x_document_entry_subject import XDocumentEntrySubject
from cdabindings.org.hl7.v3.x_document_subject import XDocumentSubject
from cdabindings.org.hl7.v3.x_information_recipient_role import XInformationRecipientRole
from cdabindings.org.hl7.v3.x_role_class_accommodation_requestor import XRoleClassAccommodationRequestor
from cdabindings.org.hl7.v3.x_role_class_coverage import XRoleClassCoverage
from cdabindings.org.hl7.v3.x_role_class_coverage_invoice import XRoleClassCoverageInvoice
from cdabindings.org.hl7.v3.x_role_class_credentialed_entity import XRoleClassCredentialedEntity
from cdabindings.org.hl7.v3.x_role_class_payee_policy_relationship import XRoleClassPayeePolicyRelationship

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ParticipantRole:
    class Meta:
        name = "POCD_MT000040.ParticipantRole"

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
    playing_device: Optional[Device] = field(
        default=None,
        metadata={
            "name": "playingDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    playing_entity: Optional[PlayingEntity] = field(
        default=None,
        metadata={
            "name": "playingEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    scoping_entity: Optional[Entity] = field(
        default=None,
        metadata={
            "name": "scopingEntity",
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
    class_code: Union[str, RoleClassMutualRelationship, RoleClassPassive, RoleClassOntological, RoleClassPartitive, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship, RoleClassRootValue] = field(
        default=RoleClassRootValue.ROL,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
