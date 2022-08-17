from dataclasses import dataclass, field
from typing import List, Optional, Union
from cda.org.hl7.v3.cs import CS
from cda.org.hl7.v3.ii import II
from cda.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cda.org.hl7.v3.null_flavor import NullFlavor
from cda.org.hl7.v3.place import Place
from cda.org.hl7.v3.role_class_mutual_relationship import RoleClassMutualRelationship
from cda.org.hl7.v3.role_class_ontological import RoleClassOntological
from cda.org.hl7.v3.role_class_partitive import RoleClassPartitive
from cda.org.hl7.v3.role_class_passive import RoleClassPassive
from cda.org.hl7.v3.role_class_root_value import RoleClassRootValue
from cda.org.hl7.v3.x_document_entry_subject import XDocumentEntrySubject
from cda.org.hl7.v3.x_document_subject import XDocumentSubject
from cda.org.hl7.v3.x_information_recipient_role import XInformationRecipientRole
from cda.org.hl7.v3.x_role_class_accommodation_requestor import XRoleClassAccommodationRequestor
from cda.org.hl7.v3.x_role_class_coverage import XRoleClassCoverage
from cda.org.hl7.v3.x_role_class_coverage_invoice import XRoleClassCoverageInvoice
from cda.org.hl7.v3.x_role_class_credentialed_entity import XRoleClassCredentialedEntity
from cda.org.hl7.v3.x_role_class_payee_policy_relationship import XRoleClassPayeePolicyRelationship

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Birthplace:
    class Meta:
        name = "POCD_MT000040.Birthplace"

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
    place: Optional[Place] = field(
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
    class_code: Union[str, RoleClassMutualRelationship, RoleClassPassive, RoleClassOntological, RoleClassPartitive, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship, RoleClassRootValue] = field(
        init=False,
        default=RoleClassPassive.BIRTHPL,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
